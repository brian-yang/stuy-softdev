var svg_panel = document.getElementById("vimage");
var move_button = document.getElementById("move");
var clear_button = document.getElementById("clear");

var svg_width = svg_panel.width.baseVal.value;
var svg_height = svg_panel.height.baseVal.value;

var radius = 10;
var velocities = [];

var requestID = 0;

function interactCircle(e) {
    if (this.getAttribute("fill") == "green") {
	this.setAttribute("fill", "pink");
    } else {
	this.remove();
	randomCircle();
    }
    e.stopPropagation();
}

function createCircle(x, y, r) {
    var circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");

    circle.setAttribute("cx", x);
    circle.setAttribute("cy", y);
    circle.setAttribute("r", r);
    circle.setAttribute("fill", "green");

    circle.addEventListener("click", interactCircle, true);

    svg_panel.appendChild(circle);
}

function regularCircle(e) {
    createCircle(e.offsetX, e.offsetY, radius);
    velocities.push([1, 1]);
}

function randomCircle(e) {
    var startX = Math.round(Math.random() * svg_width) + radius;
    var startY = Math.round(Math.random() * svg_height) + radius;

    while ( (startX + radius) >= svg_width ) {
	startX = Math.round(Math.random() * svg_width) + radius;
    }
    while ( (startY + radius) >= svg_height ) {
	startY = Math.round(Math.random() * svg_height) + radius;
    }

    createCircle(startX.toString(), startY.toString(), radius);
    velocities.push([1, 1]);
}

function circleAnimation(circle, vx, vy) {
    startX = parseInt(circle.getAttribute("cx"));
    startY = parseInt(circle.getAttribute("cy"));

    startX += vx;
    startY += vy;

    if (startX + radius > svg_width) {
	vx = -1;
    } else if (startX - radius <= 0) {
	vx = 1;
    }
    if (startY + radius > svg_height) {
	vy = -1;
    } else if (startY - radius <= 0) {
	vy = 1;
    }

    circle.setAttribute("cx", startX.toString());
    circle.setAttribute("cy", startY.toString());

    if (circle.getAttribute("cx") == svg_width / 2) {
	circle.setAttribute("r", (parseInt(circle.getAttribute("r")) / 2).toString());
	createCircle(startX.toString(), startY.toString(), circle.getAttribute("r"));
	velocities.push([-vx, -vy]);
    }
    
    return [vx, vy];
}

function moveCircles(e) {
    window.cancelAnimationFrame(requestID);
    var changeVelocity = function() {
	for (var index = 0; index < svg_panel.children.length; index++) {
	    var circle = svg_panel.children[index];
	    var vx = velocities[index][0];
	    var vy = velocities[index][1];

	    var newVelocity = circleAnimation(circle, vx, vy);
	    velocities[index] = newVelocity;

	    if (parseInt(circle.getAttribute("r")) <= 1) {
	    	circle.remove();
	    	velocities.splice(index, 1);
	    	index--;
	    }
	}
	if (svg_panel.children.length == 0) {
	    velocities = [];
	    window.cancelAnimationFrame(requestID);
	} else {
	    requestID = window.requestAnimationFrame(changeVelocity);
	}
    }
    if (svg_panel.children.length > 0) {
	changeVelocity();
    }
}

function clearSVG(e) {
    // Empty velocities
    velocities = [];
    window.cancelAnimationFrame(requestID);

    while (svg_panel.firstChild) {
	svg_panel.removeChild(svg_panel.firstChild);
    }
}

svg_panel.addEventListener("click", regularCircle);
move_button.addEventListener("click", moveCircles);
clear_button.addEventListener("click", clearSVG);
