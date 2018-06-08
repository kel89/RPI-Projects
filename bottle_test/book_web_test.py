from bottle import route, run, template, request
import time
import RPi.GPIO as GPIO

# Change these for your setup.
IP_ADDRESS = "192.168.0.194" # of your Pi

pin = 18
GPIO.setmode(GPIO.BCM) # unclear?
GPIO.setup(pin, GPIO.OUT) # sets pin as out
pwm = GPIO.PWM(pin, 500) # sets intial pwm freq (later set %'s)
pwm.start(0) # starts the light?

# Handler for the home page
@route('/')
def index():
	cmd = request.GET.get('command', '')
	if cmd == 'on':
		print("Button: light on")
		pwm.ChangeDutyCycle(100)
	elif cmd == 'off':
		print("Button: light off")
		pwm.ChangeDutyCycle(0)
	elif cmd[0:6] == "slider":
		val = cmd[6:]
		print("Slider value is:", val)
	else:
		print(cmd)
		      
	return template('home_switch.tpl')
	
	
@route('/testbutton')
def tb():
	print("test button link OK")
	return template('home_switch.tpl')	
	
@route('/<name>')
def testLink(name):
	print("Button with name", name, "was pressed")
	return template('home_switch.tpl')
	
@route('/slider/<val>')
def sliderTest(val):
	print("Linked Slider has value:", val)
	return template('home_switch.tpl')
	
@route('/testPost', method="GET")
def testPost():
	name_of_slider = request.forms.get("name")
	print(name_of_slider)
	return template('home_switch.tpl')
	
	
        
# Start the webserver running on port 80
try: 
    run(host=IP_ADDRESS, port=80)
finally:
	print("\n\n" + 40*"-")
	print("Cleaning up GPIO")
	GPIO.cleanup()
	print("Shutting down")
