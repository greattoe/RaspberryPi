const express = require('express');
const app     = express();
const http    = require('http').Server(app);
const io      = require('socket.io')(http);
const Gpio    = require('onoff').Gpio;

const sw = new Gpio(18, 'in', 'falling', {debounceTimeout: 200});

const port = 3000;
app.use(express.static(__dirname + '/public'));

var page = ['index.html', 'page2.html', 'page3.html'];
var count = 0;
var index = 0;

sw.watch( function (err, val) {
	count++;
	if( count == 999 ) count = 0;

	index = count % page.length;
	console.log( index + '.load ' + page[index] );
  
	io.emit('page', page[index]);
});

http.listen(port, function() {
  console.log('listening on *:' + port);
});