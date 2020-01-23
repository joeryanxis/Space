function setup(){
	//setInterval(getIss, 3000)
	createCanvas(windowWidth,windowHeight);
	background(0);
	fill(255);
}

function getIss(){
	loadJSON("http://api.open-notify.org/iss-now.json", visualize);
}

function visualize(data){
	var x = map(data.iss_position.longitude, 0, 200, 0, width);
	var y = map(data.iss_position.latitude, 0, 200, 0, height);
	console.log(x);
	console.log(y);
	ellipse(x,y,50,50);
}

function draw(){
	getIss();
}