<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
<meta name="viewport" contnet="width=device-width, initial-scale=1">
<style>
	
body {
	background = #CBC4AB
}

.controls {
	width: 150px;
	font-size: 32pt;
	text-align: center;
	padding: 15px;
	background-color: #44C9E8;
	color: white;
}
</style>

<script>
function sendCommand(command)
{
	$.get('/', {command: command});
}

function keyPress(event){
	code = event.keyCode;
	if (code == 111) { //on is O
		sendCommand('on');
	}
	else if (code == 102) { // of is F
		sendCommand('off');
	}
}

$(document).keypress(keyPress);

</script>
</head>
<body>

<h1>Light Switch</h1>
<button class="controls" onClick="sendCommand('on');">On</button>
<button class="controls" onClick="sendCommand('off');">Off</button>

<h1>Test Button Link</h1>
<button class="controls" id="tb">Test</button>
<script>
var but = document.getElementById("tb")
but.onclick = function() {
	location.href = "/testbutton"
}


</script>

<h1>Test Slider</h1>
<input type="range" min="1" max="100" value="50", id="testSlider">
<p>Value: <span id="val"></span></p>

<script>
var slider = document.getElementById("testSlider");
var output = document.getElementById("val")
output.innerHTML = slider.value; // show the value in the browser

slider.oninput = function(){
	// tell python what the value is
	s = "slider" + slider.value;
	sendCommand(s);
	
	//update value marker on webpage
	output.innerHTML = slider.value;
}
</script>

<h1>Test Link Button (no ajax)</h1>
<a href="/test" class="controls" style="text-decoration:none">Test</a>

<h1>Test Link Slider</h1>
<input type="range" min="1" max="100" value="50", id="linkSlider">
<p>Value: <span id="linkVal"></span></p>

<script>
var slider2 = document.getElementById("linkSlider");
var output2 = document.getElementById("linkVal");
output2.innerHTML = slider2.value;
slider2.value = slider2.value;
var val = slider2.value;
slider2.oninput = function(){
	
	//change the web page val
	output2.innerHTML = slider2.value;
	slider2.value = val;
	
	//send to new page
	s = "/slider/" + slider2.value;
	window.location.replace(s);
	slider2.value = val;
	
	
}
</script>

<h1>Test slider with POST</h1>
<form method="get" action="/testPost">
	<input name="name" type="text" </input>
</form>



<td class="controls" onClick="sendCommand('on');"></td>
<td class="controls" onClick="sendCommand('off');"></td>



</body>
</html>
