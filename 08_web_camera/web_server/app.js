var express  = require('express');
var app      = express();
var http     = require('http').Server(app);
var io       = require('socket.io')(http);
var SerialPort = require('serialport');

var sp = new SerialPort('COM10', {
  baudRate: 9600
});

var parsers    = SerialPort.parsers;
var parser     = new parsers.Readline({
  delimiter: '\r\n'
});

var port      = 3000;
var _adcValue =    0;

sp.pipe(parser);

sp.on('open', () => console.log('Port open'));

parser.on('data', function(data)
{
	//console.log(data.toString());
	if(data.substring(0,3) == "led"){
		if(data.substring(3,4) == "1")	ledStatus = "on";
		else							              ledStatus = "off";
		io.emit('led', ledStatus);
		console.log('led status: ' + ledStatus);
	}
	else if(data.substring(0,3) == "adc"){
		adcValue = data.substring(3);
		io.emit('adc', adcValue);
      if(_adcValue != adcValue) console.log('adc value: ' + adcValue);
      _adcValue = adcValue;
	}
});

app.get('/led_on',function(req,res)
{
	sp.write('led1\n\r', function(err){
		if (err) {
            return console.log('Error on write: ', err.message);
        }
        console.log('send: led on');
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('LED ON\n');
	});
});

app.get('/led_off',function(req,res)
{
	sp.write('led0\n\r', function(err){
		if (err) {
            return console.log('Error on write: ', err.message);
        }
        console.log('send: led off');
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('LED OFF\n');
	}); 
});

app.use(express.static(__dirname + '/public'));

http.listen(port, function() {  // server.listen(port, function() {
    console.log('listening on *:' + port);
});