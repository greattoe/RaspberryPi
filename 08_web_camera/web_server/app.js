const express  = require('express');
const app      = express();
const SerialPort = require('serialport');

const port      = 3000;

const sp = new SerialPort('/dev/ttyACM0', {
  baudRate: 9600
});

const maxPos   = 180;
const minPos   =   0;
const stepPos  =   5;

var posPan     =  90;
var posTilt    =  65;

app.get('/up',function(req,res)
{
    if(posTilt + stepPos <= maxPos){
        posTilt = posTilt + stepPos;
    }
    else{
        posTilt = maxPos;
    }
	sp.write('tilt'+ posTilt + '\n', function(err){
		if (err) {
            return console.log('Error on write: ', err.message);
        }
        console.log('send: ' + posTilt);
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('\n');
	});
});

app.get('/down',function(req,res)
{
    if(posTilt - stepPos >= minPos){
        posTilt = posTilt - stepPos;
    }
    else{
        posTilt = minPos;
    }
	sp.write('tilt'+ posTilt + '\n', function(err){
		if (err) {
            return console.log('Error on write: ', err.message);
        }
        console.log('send: ' + posTilt);
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('\n');
	});
});

app.get('/left',function(req,res)
{
    if(posPan + stepPos <= maxPos){
        posPan = posPan + stepPos;
    }
    else{
        posPan = maxPos;
    }
	sp.write('pan'+ posPan + '\n', function(err){
		if (err) {
            return console.log('Error on write: ', err.message);
        }
        console.log('send: ' + posPan);
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('\n');
	});
});

app.get('/right',function(req,res)
{
    if(posPan - stepPos >= minPos){
        posPan = posPan - stepPos;
    }
    else{
        posPan = minPos;
    }
	sp.write('pan'+ posPan + '\n', function(err){
		if (err) {
            return console.log('Error on write: ', err.message);
        }
        console.log('send: ' + posPan);
		res.writeHead(200, {'Content-Type': 'text/plain'});
		res.end('\n');
	});
});


app.use(express.static(__dirname + '/public'));

//http.listen(port, function() {  // server.listen(port, function() {
app.listen(port, function() {
    console.log('listening on *:' + port);
});

/*
var http     = require('http').Server(app);
var io       = require('socket.io')(http);
*/

/*
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
*/