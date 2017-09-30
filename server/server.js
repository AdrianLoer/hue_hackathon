var bodyParser = require('body-parser')
var http = require("http")
var WebSocketServer = require("ws").Server

var path = require('path');


const express = require('express');

// Constants
const PORT = 8080;

// App
const app = express();
// server = http.createServer(app);

var expressWs = require('express-ws')(app);

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies


var allowCrossDomain = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type');

    next();
}

app.use(allowCrossDomain);

app.use('/register', express.static(path.join(__dirname, "..", "Registrierung")))

app.use('/icons', express.static(path.join(__dirname, "icons")))

app.get('/', function(req, res) {
    res.send('Hello world\n');
});

app.get("/getAllUsers", function(req, res) {

    getAllUsers(function(users) {
        res.setHeader('Content-Type', 'application/json');
        res.json(users)
    })
})

app.post("/setColor", function(req, res) {
    console.log(req.body)
        if (!req.body) return res.sendStatus(400)
        if (exists(req.body)) {
        	var value = req.body.value;
        }
})

app.ws('/ws', function(ws, req) {
	console.log("echo called")
  ws.on('message', function(msg) {
  	var msgObj = {msg: msg}
  	console.log(JSON.stringify(msgObj))
    ws.send(msg);
  });
});


app.get("/map", function(req, res) {
 res.sendFile(path.join(__dirname,  "index.html"));
})



app.listen(PORT);
// server.listen(PORT);
console.log('Running on ' + PORT);

// var wss = new WebSocketServer({server: server, path: "/ws"});

// // 10.1.228.146

// wss.on("connection", function(ws) {
//    console.log("connection ");
// });


// wss.on('open', function open() {
//   ws.send('something');
// });
 
// wss.on('message', function incoming(data) {
//   console.log(data);
// });

function exists(obj) {
    return obj !== null && obj !== undefined
}