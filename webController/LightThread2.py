# LightThread2.py
# Kenneth Lipke
# July 2018

"""
This is (at first) the psuedo code and planning for an updated
light thread object, which is created in the Flask web app.
It handles *ALL* the GPIO setup (note, you may desire to change this as more
total web functionality is added).


Main Components/Functionality:
- Color Selector (with predefined colors)
- RGB Sliders for user created colors
- Dimmer (controls overall brightness)
- Commands (jump, fade, on/off)


I think the best way to handlingt he dimming is with an ultimate changer, 
i.e., every ligth change at all has to go through an ultimate function that
applies the dimmer. Into this is fed the full color, and the dimmer is
applied only there. This is also the only place that rPwr, gPwr, and bPwr 
can be touched. In their place have fields rSet, gSet, bSet, which are the
0 to 255.

For the sliders, the app can direclty call set_red, etc. They have the command
and the value, and this will take care of the dimmer.

Next, we have to thinking about jumping (fading will come next). Here is the order
to thinking about jumping:
	- Define a kill switch
	- Define a speed setting
	- Randomize colors, and change them according to time
	- If another button hit, (like a color, or fade), stop the jumping
	- When, stopped, determine how to send RGB code back to app, and through
		to the html so it shows up in the slider
"""

"""
Proposed Fields:
	+ rPwr
	+ gPwr
	+ bPwr (the above from 0 to 100, integer?) these are ONLY to be changed in ultimate changer
	+ rSet
	+ gSet
	+ bSet - these are teh RGB 0 to 256 settings for the light, these do not consider dimmer
	+ COLORS - dictionary mapping color names (str) to [r,g,b] values
	+ dim - controls brightness, serves as overall multiplier
	+ jump - boolean, serves as kill switch for light jumping
	+ spped - [0,1] multiplier controls speed of jumping and fading
"""

import RPi.GPIO as GPIO
import time
import random
import threading

class LightThread(threading.Thread):
	"""
	Put Full description here
	"""

	def __init__(self):
		# Setup GPIO:
		# define pin numbers as constants

		# Set pins as out
		# Set frequency for pins
		# Start lights at 0 (off)

		"""
		Note, here we have the following fields:
			rPwr
			gPwf
			bPwr
		These are the powers for the lights of each color, range from
		0 to 100
		"""

		# Define the color dictionary: COLORS
		# Note: we want to match this to the html file for the page

		# define dimming constrol
		# initiliaze to 0.75

	def set_red(self, r):
		"""
		Changes the red color -- Ultimate function

		Parameters
		----------
		`r` - is the [0,256] RGB value for the red component
		"""
		# save r as rSet (as still RGB number)
		# make [0,100] with (r/255)*100
		# make rPwr = dim*^^val
	# ^^Do this for all the colors

	def set_dim(self, new_dim):
		"""
		Updates the new dim settings, which requires updating the current colors
		"""
		# dim = new_dim (update value)
		# update colors to reflect this:
		# self.set_red(self.rSet) # i.e. setting it to current value,
		# however note that this time it will have a new dim
		# Do this for all the colors

	def to_color(self, color):
		"""
		Changes the lights to `color`, where `color` is a string
		that *Must* be in COLORS
		"""
		# Check that color is acceptable, if not...just print?
		vals = self.COLORS[color]
		self.set_red(vals[0])
		self.set_green(vals[1])
		self.set_blue(vals[2])








