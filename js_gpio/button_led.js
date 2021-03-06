var Gpio = require("onoff").Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(4, "out"); // out to led in GPIO port 4
var pushButton = new Gpio(17, "in", "button_press"); // it is an input, and both button presses and releases should be handled

var onoff = false; // indicates if the light is on or off

pushButton.watch(function (err, value) {
	// Watch for hardware interupts
	if (err) {
		// if there is an error alert us
		console.error("Errror!!", err) // output to console
		return;
	}
	//LED.writeSync(value); //turns on or off depending on button state
	if (onoff == false){
		LED.writeSync(1); // turn on
		onoff = true;
	}
	else{
		LED.writeSync(0); // turn off
		onoff = false;
	}
});

function unexportOnClose(){
	// function to run when exiting program
	LED.writeSync(0); // off
	LED.unexport(); // free pin
	pushButton.unexport(); // free pin
};

process.on("SIGINT", unexportOnClose); // function to run when closed via ctr+c