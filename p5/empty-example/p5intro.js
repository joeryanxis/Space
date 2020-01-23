var x,y;
var z;
function setup(){
	//Loads JSON from open-notify API
	loadJSON("http://api.open-notify.org/astros.json", visualize);
	createCanvas(windowWidth, windowHeight);
	textSize(32);
}

//Callback function from our loadJSON
function visualize(data){
	background(0);
	console.log(data.number);

	
	
	for(var i=0; i<data.number; i++){
		x = random(0,width);
		y = random(0,height);
		ellipse(x, y, 30, 30);
		
		text(data.people[i].name,x+20,y+20);
		console.log(data.people[i].name);
	}
}