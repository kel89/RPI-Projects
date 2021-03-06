var Gpio = require("onoff").Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(4, "out"); // out to led in GPIO port 4
var blinkInterval = setInterval(blinkLED, 250); // run the blinkLED function every 250 ms
//blinkLED()

function blinkLED(){
	// check the pin state, it is 0 if the LED is off
	if (LED.readSync() === 0){
		// if it is off, turn it on
		LED.writeSync(1); 
	}
	else{
		// else it is on, so turn it off
		LED.writeSync(0);
	}
}

function endBlink(){
	// function to stop blinking
	clearInterval(blinkInterval); // stops blink intervals
	LED.writeSync(0); // turns LED off
	LED.unexport(); // unexport GPIO to free resources (not sure?)
}
	
setTimeout(endBlink, 5000); // quits the program after 5 seconds