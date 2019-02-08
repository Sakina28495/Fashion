/*var AssistantV2 = require('watson-developer-cloud/assistant/v2');

var assistant = new AssistantV2({
  version: '2018-11-08',
  iam_apikey: 's2JwNm1emTHhuqHK4dyLU1GLPldYl3qMIHxmUclX5arw',
  url: 'https://gateway.watsonplatform.net/assistant/api'
});

assistant.method(params,
  function (err, response) {
    // The error will be the first argument of the callback
    if (err.code == 404) {

      // Handle Not Found (404) error
    } else if (err.code == 413) {

      // Handle Request Too Large (413) error
    } else {
      console.log('Unexpected error: ', err.code);
      console.log('error:', err);
    }
  });

assistant.methodName({
  parameters,
  headers: {
    'Custom-Header': '{header_value}'
  }
},
  function (err, response) {
    if (err) {
      console.log('error:', err);
    } else {
      console.log(response);
    }
  }
);


assistant.methodName({
  parameters
},
  function (err, result, response) {
    if (err) {
      console.log('error:', err);
    } else {
      console.log(response.headers);
    }
  }
);

var AssistantV2= require('watson-developer-cloud/');

var assistant = new AssistantV2({
    version: '2018-11-08',
  iam_apikey: 's2JwNm1emTHhuqHK4dyLU1GLPldYl3qMIHxmUclX5arw',
  headers: {
    'X-Watson-Learning-Opt-Out': 'true'
  }
});*/


/*var watson = require('watson-developer-cloud');

var service = new watson.AssistantV2({
  iam_apikey: 's2JwNm1emTHhuqHK4dyLU1GLPldYl3qMIHxmUclX5arw',
  version: '2018-11-08',
  url: 'https://gateway-syd.watsonplatform.net/assistant/api'
});

service.createSession({
  assistant_id: '2a8e1033-05dc-47c6-9eb1-20730ff217ff',
}, function(err, response) {
  if (err) {
    console.error(err);
  } else{
    console.log(JSON.stringify(response, null, 2));
  }
});*/

'use strict';

var express = require('express'); // app server
var bodyParser = require('body-parser'); // parser for post requests
var AssistantV2 = require('watson-developer-cloud/assistant/v2'); // watson sdk
const util = require('util')
var app = express();

// Bootstrap application settings
app.use(express.static('./public')); // load UI from public folder
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

var mongoose = require("mongoose");
mongoose.Promise = global.Promise;
mongoose.connect("mongodb://localhost:27017/IBMWatson");

var watsonSchema = new mongoose.Schema({
  input: String,
  intent: String,
  entity: String
});

var Assistant = mongoose.model("Assistant", watsonSchema);

// Create the service wrapper

var newContext = {
  global : {
    system : {
      turn_count : 1
    }
  }
};


var watson = require('watson-developer-cloud');
var s_id;
var service = new watson.AssistantV2({
 iam_apikey: 's2JwNm1emTHhuqHK4dyLU1GLPldYl3qMIHxmUclX5arw',
  version: '2018-11-08',
  url: 'https://gateway-syd.watsonplatform.net/assistant/api'
});

service.createSession({
  assistant_id: '2a8e1033-05dc-47c6-9eb1-20730ff217ff',
}, function(err, response) {
  if (err) {
    console.error(err);
  } else{
    s_id = response.session_id;

  }

})

/*var button = document.getElementById('myButton');
button.addEventListener('click', function(e) {
  console.log('button was clicked');

  fetch('/clicked', {method: 'POST'})
    .then(function(response) {
      if(response.ok) {
        console.log('click was recorded');
        return;
      }
      throw new Error('Request failed.');
    })
    .catch(function(error) {
      console.log(error);
    });
});

app.post('/clicked', (req, res) => {
  var myValue = new Assistant({
    input : req.body.input.text
  });

  myValue.save(function(err) {
        if (err)
           throw err;
        else 
           console.log('save user successfully...');
    });

  
  });*/

// Endpoint to be call from the client side
app.post('/api/message', function (req, res) {
          var i=0,j=0,r="";
          var k="";

/*var myValue = new Assistant({
    input : req.body.input.text
   // intent: 
  });

  myValue.save(function(err) {
        if (err)
           throw err;
        else 
           {console.log('save user successfully...');
       console.log(req.body.input.text);
       }

    });*/

  
    service.message({
      assistant_id: '2a8e1033-05dc-47c6-9eb1-20730ff217ff',
      session_id: s_id ,
      input: {
        //'message_type': 'text',
        'text': req.body.input.text}
    }, function(err, response) {
      if (err)
        console.log('error:', err);
      else
      {
        if(req.body.input.text != null)
        console.log("Input Text :",req.body.input.text);
    	if(response.output.intents[i]  != null)
        {
          var k=response.output.intents[i].intent;
    			console.log("Intent detected :",response.output.intents[i].intent);	

        }
        
        if(response.output.entities[i] != null)
        {
            var r=response.output.entities[i].value;
        		console.log("Entity" + "  " + j + "  " + "detected :",r);
        }  
var myValue = new Assistant({
    input : req.body.input.text,
   intent : k,
   entity : r
  });

  myValue.save(function(err) {
        if (err)
           throw err;
        else 
           {console.log('save user successfully...');
       console.log(req.body.input.text);
      // console.log(output.intents[i].intent);
      // console.log(response.output.entities[i].value);
       }

    });
             
      }
      console.log(" ");
       // console.log(util.inspect(response, {showHidden: false, depth: null}))
       //console.log(req.body);
       // console.log(JSON.stringify(response, null, 2));   
    
});

  });
/*app.post("/sendData", (req, res) => {
 var myValue = new Assistant(req.body);
  myValue.save()
    .then(item => {
      res.send("item saved to database");
    })
    .catch(err => {
      res.status(400).send("unable to save to database");
    });
});*/


app.get('/api/session', function (req, res) {
  service.createSession({
    assistant_id: process.env.ASSISTANT_ID || '{assistant_id}',
  }, function (error, response) {
    if (error) {
      return res.send(error);
    } else {
      return res.send(response);
    }
  });
});


module.exports = app;
