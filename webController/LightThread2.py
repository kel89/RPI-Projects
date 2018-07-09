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
Now, if the user selects a new color, or moves the slider, before hitting
the stop jump button, we need to stop the jumping, withough adjusting the sliders.
with the `keep_jumping` options, we can simply OMIT them in the call from the 
app. This way, if a slider is adjusted, or a button pressed in the app, automatically
keep_jumping will be False, and the jumping will stop. (We can do something
similar for the fading when we get that figured out)

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

		# initliaze for jump
		jump = False
		speed = 0.5 # play with this <----------

	def set_red(self, r, keep_jumping=False):
		"""
		Changes the red color -- Ultimate function

		Parameters
		----------
		`r` - is the [0,256] RGB value for the red component
		"""
		# if not keep_jumping and jump is True
		# set jump to false (flip the switch)


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

	def to_color(self, color, keep_jumping=False):
		"""
		Changes the lights to `color`, where `color` is a string
		that *Must* be in COLORS
		"""
		# if not keep_jumping AND jump is True
		# i.e. we don't want to keep jumping but we currently are
		# set jump to false

		# Check that color is acceptable, if not...just print?
		vals = self.COLORS[color]
		self.set_red(vals[0], keep_jumping)
		self.set_green(vals[1], keep_jumping)
		self.set_blue(vals[2], keep_jumping)

	def start_jump(self):
		"""
		Starts and controls jumping for lights
		-------
		UPDATE THIS WHEN IT IS WRITTEN/PSUEDO CODE DONE
		"""

		# set swtich to on
		jump = True

		# Start jumping loop
		while jump:
			# choose a random color from the dictionary
			# change to that color with to_color (with keep_jumping=True)
			# wait according to the speed timer <-------------- requires tweaking


	def stop_jump(self):
		"""
		Stops the jumping -- to be called when the button is explicitly
		hit to stop the jumping
		-------
		UPDATE THIS WHEN IT IS WRITTEN/PSUEDO CODE DONE
		"""

		# flip the jump switch
		jump = False 

		# Now get the current color, in RGB form and return it as a dictionary
		# so that it can be sent JQURY style to update the sliders
		current = {
			"red":str(self.rSet),
			"green":str(self.gSet),
			"blue":str(self.bSet)
		}
		return current
		# Note, this will require the html/js to be updated so that the jump
		# button is bound to a getJSON

	NOW THING ABOUT FADING






