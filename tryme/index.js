#!/usr/bin/env node
 
var express = require('express');
var bodyParser = require('body-parser');
var request = require('request-promise');
 
var app = express();
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
 
app.get('/postdatatoFlask', async function (req, res) {
    var data = { // this variable contains the data you want to send
        data1: "foo",
        data2: "bar"
    }
 
    var options = {
        method: 'POST',
        uri: 'http://127.0.0.1:5000/postdatatoFlask',
        body: data,
        json: true // Automatically stringifies the body to JSON
    };
    
    var returndata;
    var sendrequest = await request(data)
    .then(function (parsedBody) {
        console.log(parsedBody); // parsedBody contains the data sent back from the Flask server
        returndata = parsedBody; // do something with this data, here I'm assigning it to a variable.
    })
    .catch(function (err) {
        console.log(err);
    });
    
    res.send(returndata);
});

app.listen(3000);