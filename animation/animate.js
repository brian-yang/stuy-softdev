var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

var circle = document.getElementById('circle');
var dvd = document.getElementById('DVD');
var stop = document.getElementById('stop');

ctx.fillStyle = "#7F9299";

var requestID = 0;
// =============================================
function circleAnimation(e) {
    // Reset
    var radius = 0;
    var incFactor = 1;
    window.cancelAnimationFrame(requestID);

    var drawCircle = function() {
	// Clear
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	// Draw circle
	ctx.beginPath();
	ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, 2 * Math.PI);
	ctx.fill();
	ctx.stroke();
	ctx.closePath();

	// Shrink/expand
	radius += incFactor;
	if (radius > canvas.width / 2 || radius > canvas.height / 2) {
	    incFactor = -1;
	} else if (radius <= 0) {
	    incFactor = 1;
	}

	requestID = window.requestAnimationFrame(drawCircle);
    }
    drawCircle();
}
// =============================================
var img = new Image();
img.src = "dvd.png";

// img width = 1280
// img height = 792
// scaled down to fit canvas
var width = 1280 / 10;
var height = 792 / 10;

function DVDAnimation(e) {
    var startX = Math.round(Math.random() * canvas.width);
    var startY = Math.round(Math.random() * canvas.height);
    var incX = 1;
    var incY = 1;

    // Reset
    while ( (startX + width) > canvas.width ) {
	startX = Math.round(Math.random() * canvas.width);
    }
    while ( (startY + height) > canvas.height ) {
	startY = Math.round(Math.random() * canvas.height);
    }

    window.cancelAnimationFrame(requestID);

    var drawDVD = function() {
	// Clear
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	ctx.drawImage(img, startX, startY, width, height);

	startX += incX;
	startY += incY;
	if (startX + width > canvas.width) {
	    incX = -1;
	} else if (startX <= 0) {
	    incX = 1;
	}
	if (startY + height > canvas.height) {
	    incY = -1;
	} else if (startY <= 0) {
	    incY = 1;
	}

	requestID = window.requestAnimationFrame(drawDVD);
    }
    drawDVD();
}

// =============================================
function stopAnimation(e) {
    window.cancelAnimationFrame(requestID);
}
// =============================================
circle.addEventListener('click', circleAnimation);
dvd.addEventListener('click', DVDAnimation);
stop.addEventListener('click', stopAnimation);
