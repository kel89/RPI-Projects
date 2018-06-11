# controller v2
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

NEW IN V2: use of a lightThread which controls all lighting, this is
created in the begining. This is meant to allow for jumping and fading
and as a way to future proof when we later add other controller features
"""

from flask import Flask, render_template, flash, request, sessions, abort
import RPi.GPIO as GPIO
import time
import random
import threading

from lightThread import * # the lightThread class


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


if __name__ == "__main__":
	# Run the app
	app.run(debug=True, host="0.0.0.0", use_reloader=False, threaded=True)

	# Runs when the server is stopped (ctr + c)
	print("\n\n")
	print(80*"-")
	print("Quitting") 
	
	# Put GPIO cleanup here
	GPIO.cleanup()
	print("GPIO cleaned")


