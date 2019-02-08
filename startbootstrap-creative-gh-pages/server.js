'use strict';

require('dotenv').config({silent: true});

var server = require('./app');
var port = process.env.PORT || 4000;

server.listen(port, function() {
  // eslint-disable-next-line
  console.log('Server running on port: %d', port);
});


/*var express = require('express');
var app = express();
var port = 4000;

app.use("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});
 
app.listen(port, () => {
  console.log("Server listening on port " + port);
});*/