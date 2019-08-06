const express = require('express');

const app = express();
const port = 8000;

const Gpio = require('onoff').Gpio;
const red = new Gpio(23, 'out');
const grn = new Gpio(24, 'out');

app.use(express.static(__dirname + '/public'));

app.get('/red_on', function(req, res) {
	red.writeSync(1);
	console.log('send: led red on');
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('LED Red On\n');
});

app.get('/red_off', function(req, res) {
	red.writeSync(0);
	console.log('send: led red off');
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('LED Red Off\n');
});

app.get('/green_on', function(req, res) {
	grn.writeSync(1);
	console.log('send: led green on');
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('LED Green On\n');
});

app.get('/green_off', function(req, res) {
	grn.writeSync(0);
	console.log('send: led green off');
	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end('LED Green Off\n');
});

app.listen(port, function(err) {
  console.log('Connected port - ' + port);
  if (err) {
    return console.log('Found error - ', err);
  }
});