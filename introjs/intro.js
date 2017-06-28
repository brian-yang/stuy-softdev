var button = document.getElementById('b');
var cutton = document.getElementById('c');
var list = document.getElementById('thelist');
var mist = document.getElementById('themist');
var heading = document.getElementById('h');

var addListItemListeners = function (item) {
	item.addEventListener('mouseover', function (e) {
		heading.innerText = this.innerText;
		console.log(heading.innerText);
	});

	item.addEventListener('click', function (e) {
		this.remove();
	});
};

button.addEventListener('click', function (e) {
	var item = document.createElement('li');
	var text = document.createTextNode('new item');
	item.appendChild(text);
	addListItemListeners(item);
	list.appendChild(item);
});

var listItems = document.getElementsByTagName('li');

for (var i = 0; i < listItems.length; i++) {
	var item = listItems[i];
	addListItemListeners(item);
}

var f1 = 0;
var f2 = 1;

cutton.addEventListener('click', function (e) {
	var item = document.createElement('li');
	var text = document.createTextNode(f1);
	console.log(f1 + ' ' + f2);
	item.appendChild(text);
	mist.appendChild(item);

	f2 += f1;
	f1 = f2 - f1;
});
