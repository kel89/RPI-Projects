# controller.py
# Kenneth Lipke
# Summer 2018

"""
Flask web app for Raspberry pi that controlls GPIO's to turn on
lights etc.

takes templates (html files) from the templates folder,
and .css files from that static folder. These however hace an issue
with browser caching, and therefore will not update unless the name
is changes, therefore I will put al style in the header of the html file
and or use an outside framework, i.e. bootstrap
"""

from flask import Flask, render_template, flash, request, sessions, abort
import RPi.GPIO as GPIO
import time
import random
import threading
from multiprocessing import Process, Value


class lightThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.kill = False
	
	def run_jump(self):
		num_colors = len(colors.keys())
		keys = list(colors.keys())
		i = 0
		while not self.kill:
			color = keys[i]
			print("Trying to change color to", color)
			change_color(color)
			time.sleep(1)
			i = (i + 1)%num_colors
			
	def quit(self):
		self.kill = True

def jump():		
	num_colors = len(colors.keys())
	keys = list(colors.keys())
	i = 0
	while True:
		color = keys[i]
		print("Trying to change color to", color)
		change_color(color)
		time.sleep(1)
		i = (i + 1)%num_colors
# initialize process	
jump_p = Process(target=jump)

# set up GPIO and pins
RPIN = 18
GPIN = 23
BPIN = 24

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RPIN, GPIO.OUT)
GPIO.setup(GPIN, GPIO.OUT)
GPIO.setup(BPIN, GPIO.OUT)

redPwr = GPIO.PWM(RPIN, 1000)
bluePwr = GPIO.PWM(BPIN, 1000)
greenPwr = GPIO.PWM(GPIN, 1000)

redPwr.start(0)
bluePwr.start(0)
greenPwr.start(0)

# Create holders to always store current value
red_duty = 0
green_duty = 0
blue_duty = 0

jump_thread = lightThread(1, "test") # global jump thread holder

def update_red(duty):
	new = float(duty)
	redPwr.ChangeDutyCycle(new)
	global red_duty
	red_duty = new
def update_green(duty):
	new = float(duty)
	greenPwr.ChangeDutyCycle(new)
	global green_duty
	green_duty = new
def update_blue(duty):
	new = float(duty)
	bluePwr.ChangeDutyCycle(new)
	global blue_duty
	blue_duty = new
	
def rgb_to_pct(num):
	"""
	changes rgb number (0,256) to a % number (0 to 100)
	"""
	return int(80*num/256)
	
def change_color(cmd):
	"""
	changes light color according to the command
	"""
	# get color code
	rgb = colors[cmd]
	
	# map to duties
	duty = [rgb_to_pct(x) for x in rgb]
	
	update_red(duty[0])
	update_green(duty[1])
	update_blue(duty[2])
	print("color updated")
	
def light_off():
	"""turns light off"""
	update_red(0)
	update_green(0)
	update_blue(0)
	
def adjust_brightness(level):
	"""
	adjusts brightness across all colors
	"""
	level = float(level/100) # make sure between 0 and 1
	print("Level multiplier is", level)
	update_red(level*red_duty)
	print("New red duty is", level*red_duty)
	update_green(level*green_duty)
	update_blue(level*blue_duty)
	print("Brigthness updated")
	
	
# Color Dictionary ----------------
colors = {"blue":[0,0,256], "red":[256,0,0], "green":[0,256,0],
			"yellow":[255,255,0], "orange":[255,255,0], "purple":[138,43,226],
			"pink":[255,105,180], "springgreen":[0,255,127],
			"turquoise":[64,224,208]}

# Create the app
app = Flask(__name__)

def get_cmd():
	"""
	returns the GET command sent via Jquery from the page
	"""
	a = request.args
	cmd = None
	try:
		cmd = a['command']
	except:
		cmd = None

	return cmd



# root route
@app.route("/", methods=["GET"]) # get so it can handle jquery
def index():
	# what it should do
	cmd = get_cmd()
	print(cmd)
	
	# Change to pre-specified color
	if cmd in colors.keys():
		change_color(cmd)
		
	# Turn off
	if cmd == "off":
		print("trying to shutdown")
		light_off()
		
		if jump_p.is_alive():
			print("Terminating the process")
			jump_p.terminate()
		
		# check if threads on
		if jump_thread.kill == False:
			print("Trying to kill")
			jump_thread.quit()
			# create a new process for next time
			global jump_p
			jump_p = Process(target=jump)
			
				
		
	# Check Color Slider
	if cmd is not None:
		if cmd[0:2]=="R:":
			update_red(rgb_to_pct(int(cmd[2:]))) # update red
		elif cmd[0:2]=="G:":
			update_green(rgb_to_pct(int(cmd[2:]))) # update green
		elif cmd[0:2]=="B:":
			update_blue(rgb_to_pct(int(cmd[2:]))) # update blue
			
	# Check Brightness slider
	if cmd is not None:
		if cmd[0:7] == "Bright:":
			print("Detected brightness command")
			adjust_brightness(int(cmd[7:]))
			
	# Jump command
	if cmd == "jump":
		#print("\n\nabout to run the jump")
		#global jump_thread
		#jump_thread.run_jump()
		#print("\nWe have moved past the run jump")
		print("Starting the process?")
		jump_p.start()
	
	

	return render_template("index.html") # where index.html is in templates





			


if __name__ == "__main__":
	# Run the app
	app.run(debug=True, host="0.0.0.0", use_reloader=False)

	# Runs when the server is stopped (ctr + c)
	print("\n\n")
	print(80*"-")
	print("Quitting") 
	
	# Put GPIO cleanup here
	GPIO.cleanup()
	print("GPIO cleaned")
