var container = document.getElementById("vimage");
var x = container.getAttribute("width")/2;
var y = container.getAttribute("height")/2;
buttonDiv = document.getElementById("roomButtons");
whichRoom = document.getElementById("whichRoom");
var redRooms = ""

var link = window.location['href']
console.log(link);

var apple = link.split("/")
console.log(apple);
var date = apple[apple.length-2];


var actionLink =  "/reserve/" + date + "/"
whichRoom.setAttribute("action", actionLink);
console.log(actionLink);

function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    	redRooms += this.responseText;
    }
  };
  xhttp.open("GET", "/redRooms/" + date + "/", true);
  xhttp.send();
}


var drawMap = function() {
	//outgrowth where 411 and 413 are
	var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
	line.setAttribute("x1", 290);
	line.setAttribute("y1", 0);
	line.setAttribute("x2", 290);
	line.setAttribute("y2", 60);
	line.setAttribute("style","stroke:black;stroke-width:2");
	container.appendChild(line);

	var room = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room.setAttribute("x", 310);
	room.setAttribute("y", 30);
	room.innerHTML = "313";
	room.setAttribute("fill", "blue");
	room.setAttribute("font-size", "16px");
	container.appendChild(room);

	var roomBox = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox.setAttribute("x", 297)
	roomBox.setAttribute("y", 10)
	roomBox.setAttribute("rx", 5)
	roomBox.setAttribute("id", "313");
	roomBox.setAttribute("ry", 5)
	roomBox.setAttribute("width", 50);
	roomBox.setAttribute("height", 40);
	container.appendChild(roomBox);

	
	var line1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
	line1.setAttribute("x1", 290);
	line1.setAttribute("y1", 60);
	line1.setAttribute("x2", 440);
	line1.setAttribute("y2", 60);
	line1.setAttribute("style","stroke:black;stroke-width:2");
	container.appendChild(line1);
	
	var room1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room1.setAttribute("x", 380);
	room1.setAttribute("y", 30);
	room1.innerHTML = "315";
	room1.setAttribute("fill", "blue");
	room1.setAttribute("font-size", "16px");
	container.appendChild(room1);

	var roomBox1 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox1.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox1.setAttribute("x", 370)
	roomBox1.setAttribute("y", 10)
	roomBox1.setAttribute("rx", 5)
	roomBox1.setAttribute("ry", 5)
	roomBox1.setAttribute("id", "315")
	roomBox1.setAttribute("width", 50);
	roomBox1.setAttribute("height", 40);
	container.appendChild(roomBox1);

	
	var line2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
	line2.setAttribute("x1", 440);
	line2.setAttribute("y1", 60);
	line2.setAttribute("x2", 440);
	line2.setAttribute("y2", 0);
	line2.setAttribute("style","stroke:black;stroke-width:2");
	container.appendChild(line2);





	//two boxy things
	var escalator = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator.setAttribute("x", 150)
	escalator.setAttribute("y", 150)
	escalator.setAttribute("width", 270);
	escalator.setAttribute("height", 75);
	container.appendChild(escalator);

	var escalator1 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	escalator1.setAttribute("style", "fill:black;stroke:black;stroke-width");
	escalator1.setAttribute("x", 530)
	escalator1.setAttribute("y", 110)
	escalator1.setAttribute("width", 260);
	escalator1.setAttribute("height", 135);
	container.appendChild(escalator1);




	//403
	var room3 = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room3.setAttribute("x", 66);
	room3.setAttribute("y", 20);
	room3.innerHTML = "303";
	room3.setAttribute("fill", "blue");
	room3.setAttribute("font-size", "16px");
	container.appendChild(room3);

	var roomBox3 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox3.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox3.setAttribute("x", 56)
	roomBox3.setAttribute("y", 1)
	roomBox3.setAttribute("rx", 5)
	roomBox3.setAttribute("ry", 5)
	roomBox3.setAttribute("id", "303");
	roomBox3.setAttribute("width", 50);
	roomBox3.setAttribute("height", 40);
	container.appendChild(roomBox3);


	//405
	var room4 = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room4.setAttribute("x", 119);
	room4.setAttribute("y", 20);
	room4.innerHTML = "305";
	room4.setAttribute("fill", "blue");
	room4.setAttribute("font-size", "16px");
	container.appendChild(room4);

	var roomBox4 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox4.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox4.setAttribute("x", 110)
	roomBox4.setAttribute("y", 1)
	roomBox4.setAttribute("rx", 5)
	roomBox4.setAttribute("ry", 5)
	roomBox4.setAttribute("id", "305")
	roomBox4.setAttribute("width", 50);
	roomBox4.setAttribute("height", 40);
	container.appendChild(roomBox4);



	//440
	var room6 = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room6.setAttribute("x", 539);
	room6.setAttribute("y", 95);
	room6.innerHTML = "Photo Room";
	room6.setAttribute("fill", "blue");
	room6.setAttribute("font-size", "16px");
	container.appendChild(room6);

	var roomBox6 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox6.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox6.setAttribute("x", 530)
	roomBox6.setAttribute("y", 68)
	roomBox6.setAttribute("rx", 5)
	roomBox6.setAttribute("ry", 5)
	roomBox6.setAttribute("id", "photo")
	roomBox6.setAttribute("width", 105);
	roomBox6.setAttribute("height", 40);
	container.appendChild(roomBox6);

	//loop for the others
	var starter = 325;
	var xS = 450;
	var xT = 445;
	for (i = 0; i < 8; i++) {
		var room5 = document.createElementNS("http://www.w3.org/2000/svg", "text");
		room5.setAttribute("x", xS );
		room5.setAttribute("y", 25);
		room5.innerHTML = starter.toString();
		room5.setAttribute("fill", "blue");
		room5.setAttribute("font-size", "16px");
		container.appendChild(room5);
		starter += 2;
		
		var roomBox3 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
		roomBox3.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
		roomBox3.setAttribute("x", xT)
		roomBox3.setAttribute("y", 5)
		roomBox3.setAttribute("rx", 5)
		roomBox3.setAttribute("ry", 5)
		roomBox3.setAttribute("id", starter.toString());
		roomBox3.setAttribute("width", 45);
		roomBox3.setAttribute("height", 40);
		container.appendChild(roomBox3);
		xS += 51;
		xT += 51;
	}

	//450
	var room7 = document.createElementNS("http://www.w3.org/2000/svg", "text");
	room7.setAttribute("x", 565);
	room7.setAttribute("y", 330);
	room7.innerHTML = "351";
	room7.setAttribute("fill", "blue");
	room7.setAttribute("font-size", "16px");
	container.appendChild(room7);

	var roomBox7 = document.createElementNS("http://www.w3.org/2000/svg", "rect");
	roomBox7.setAttribute("style", "fill:white;fill-opacity:0;stroke:black;stroke-width");
	roomBox7.setAttribute("x", 555)
	roomBox7.setAttribute("y", 305)
	roomBox7.setAttribute("rx", 5)
	roomBox7.setAttribute("ry", 5)
	roomBox7.setAttribute("id", "351")
	roomBox7.setAttribute("width", 50);
	roomBox7.setAttribute("height", 40);
	container.appendChild(roomBox7);

	//ATRIUM SIGN
	var atrium = document.createElementNS("http://www.w3.org/2000/svg", "text");
	atrium.setAttribute("x", 95);
	atrium.setAttribute("y", 300);
	atrium.innerHTML = "Atrium 	&#8711;";
	atrium.setAttribute("fill", "blue");
	atrium.setAttribute("font-size", "20px");
	container.appendChild(atrium);

	//GYM SIGN
	var gym = document.createElementNS("http://www.w3.org/2000/svg", "text");
	gym.setAttribute("x", 30);
	gym.setAttribute("y", 255);
	gym.innerHTML = "&#8826 Gym";
	gym.setAttribute("fill", "blue");
	gym.setAttribute("font-size", "20px");
	container.appendChild(gym);



}

var del = function() {
    $.ajax({
        url: '/redRooms/' + date + "/",
        data: $('form').serialize(),
        type: 'GET',
        success: function(data) {
        	p = data.split("*")
        	console.log(p)
        	g = $("div.rooms1").find("button");
        	for (var i = 0; i < g.length; i++) {
        		console.log(g[i].innerHTML)
        		if (p.indexOf(g[i].innerHTML) > -1) {
        			g[i].remove()
        		}
            }
        },
        error: function(error) {
           		console.log(error);
           		} 
    });
}


function main() {
	del();
	drawMap();
}

$(document).ready(function () {
   main();
});