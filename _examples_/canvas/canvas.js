var canvas = document.getElementById('canvas')
var ctx = canvas.getContext('2d')

ctx.beginPath();
ctx.arc(canvas.width / 2, canvas.height / 2, 50, 0, 2 * Math.PI);
ctx.closePath();
