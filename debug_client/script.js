$(document).ready(function() {
	// Create WebSocket connection.
const socket = new WebSocket('ws://192.168.0.100:80/ws');

// Connection opened
socket.addEventListener('open', function (event) {
    socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', function (event) {
    // console.log(JSON.stringify(event.data));
    setCanvas(JSON.parse(event.data).msg)
});

setCanvas()
var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");


function setCanvas(base64string) {

var image = new Image();
image.onload = function() {
	// console.log(image.height)
    ctx.drawImage(image, 0, 0);
};
image.src = "data:image/png;base64," + base64string;
}







})
