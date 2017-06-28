var svg_panel = document.getElementById("vimage");

var circle = document.getElementById('circle');
var dvd = document.getElementById('DVD');
var stop = document.getElementById('stop');

var svg_width = svg_panel.width.baseVal.value;
var svg_height = svg_panel.height.baseVal.value;

var requestID = 0;
// =============================================
function circleAnimation(e) {
    // Reset
    var radius = 0;
    var incFactor = 1;
    window.cancelAnimationFrame(requestID);

    var drawCircle = function() {
	// Clear
	clearSVG();

	// Draw circle
	circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");

	circle.setAttribute("cx", svg_width / 2);
	circle.setAttribute("cy", svg_height / 2 );
	circle.setAttribute("r", radius.toString());

	circle.setAttribute("fill", "orange");

	svg_panel.appendChild(circle);

	// Shrink/expand
	radius += incFactor;
	if (radius > svg_width / 2 || radius > svg_height / 2) {
	    incFactor = -1;
	} else if (radius <= 0) {
	    incFactor = 1;
	}

	requestID = window.requestAnimationFrame(drawCircle);
    }
    drawCircle();
}
// =============================================
// img width = 1280
// img height = 792
// scaled down to fit canvas
var width = 1280 / 10;
var height = 792 / 10;

function DVDAnimation(e) {
    var startX = Math.round(Math.random() * svg_width);
    var startY = Math.round(Math.random() * svg_height);
    var incX = 1;
    var incY = 1;

    // Reset
    while ( (startX + width) > svg_width ) {
	startX = Math.round(Math.random() * svg_width);
    }
    while ( (startY + height) > svg_height ) {
	startY = Math.round(Math.random() * svg_height);
    }

    window.cancelAnimationFrame(requestID);

    var genImage = function() {
	var dvdsvg = document.createElementNS('http://www.w3.org/2000/svg','image');

	dvdsvg.setAttribute('width', width.toString());
	dvdsvg.setAttribute('height', height.toString());
	dvdsvg.setAttribute('x', startX);
	dvdsvg.setAttribute('y', startY);
	dvdsvg.setAttribute('href', 'dvd.png');

	svg_panel.appendChild(dvdsvg);
    }

    var drawDVD = function() {
	// Clear
	clearSVG();

	genImage();

	startX += incX;
	startY += incY;
	if (startX + width > svg_width) {
	    incX = -1;
	} else if (startX <= 0) {
	    incX = 1;
	}
	if (startY + height > svg_height) {
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

function clearSVG(e) {
    while (svg_panel.firstChild) {
	svg_panel.removeChild(svg_panel.firstChild);
    }
}
// =============================================
circle.addEventListener('click', circleAnimation);
dvd.addEventListener('click', DVDAnimation);
stop.addEventListener('click', stopAnimation);
