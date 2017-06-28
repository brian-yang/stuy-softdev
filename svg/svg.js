var svg_panel = document.getElementById("vimage");
var clear_button = document.getElementById("clear");
var circle;
var line;

var lineX = -1;
var lineY = -1;
function createCircle(e) {
    circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");

    circle.setAttribute("cx", e.offsetX.toString());
    circle.setAttribute("cy", e.offsetY.toString());
    circle.setAttribute("r", "10");

    if (lineX != -1 && lineY != -1) {
	line = document.createElementNS("http://www.w3.org/2000/svg", "line");

	line.setAttribute("x1", lineX);
	line.setAttribute("y1", lineY);    
	line.setAttribute("x2", e.offsetX.toString());
	line.setAttribute("y2", e.offsetY.toString());

	line.setAttribute("style","stroke: black");

	svg_panel.appendChild(line);
    }

    lineX = e.offsetX;
    lineY = e.offsetY;
    
    svg_panel.appendChild(circle);
}
function clearSVG(e) {
    while (svg_panel.firstChild) {
	svg_panel.removeChild(svg_panel.firstChild);
    }
    lineX = -1;
    lineY = - 1;
}
svg_panel.addEventListener("click", createCircle);
clear_button.addEventListener("click", clearSVG);
