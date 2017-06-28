var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

var clear_button = document.getElementById('clear');

// Rectangle that canvas
function drawRectangle(e) {
    ctx.fillStyle = "#CFA3A3";
    ctx.fillRect(e.offsetX, e.offsetY, 30, 30);
}

var first_circle = true;
var startX = 0;
var startY = 0;
// Connect the dots
function drawCircle(e) {
    ctx.fillStyle = "#CFA3A3";
    if (first_circle) {
	ctx.beginPath();
	ctx.arc(e.offsetX, e.offsetY, 30, 0, 2 * Math.PI);
	ctx.fill();
	ctx.stroke();
	ctx.closePath();

	first_circle = false;
    } else {
	ctx.beginPath();
	ctx.moveTo(startX, startY);
	ctx.lineTo(e.offsetX, e.offsetY);
	ctx.stroke();
	ctx.closePath();

	ctx.beginPath();
	ctx.arc(e.offsetX, e.offsetY, 30, 0, 2 * Math.PI);
	ctx.fill();
	ctx.stroke();
	ctx.closePath();
    }
    startX = e.offsetX;
    startY = e.offsetY;
}

function clearCanvas(e) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    first_circle = true; // comment out if drawing rectangles
}

canvas.addEventListener('click', drawCircle);
clear_button.addEventListener('click', clearCanvas);
