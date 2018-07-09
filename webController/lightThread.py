# lightThread.py
# Kenneth Lipke
# Summer 2018


"""
File contraining the lightThread class, a subclass of threading.Thread
This controlls all lights in a seperate thread, that can run in the 
background with Flask, so it can run on a constant loop and the program
can still take jquery updates
"""

import RPi.GPIO as GPIO
import time
import random
import threading

class lightThread(threading.Thread):
	def __init__(self):
		# Main initializers
		threading.Thread.__init__(self)
		self.kill = False
		self.jump_pause = 0.5 # starting speed (pause down, speed up)

		# GPIO initialization
		RPIN = 18
		GPIN = 23
		BPIN = 24

		# Setup GPIO
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(RPIN, GPIO.OUT)
		GPIO.setup(GPIN, GPIO.OUT)
		GPIO.setup(BPIN, GPIO.OUT)

		# Set frequency
		self.redPwr = GPIO.PWM(RPIN, 1000)
		self.bluePwr = GPIO.PWM(BPIN, 1000)
		self.greenPwr = GPIO.PWM(GPIN, 1000)

		# Start lights off
		self.redPwr.start(0)
		self.bluePwr.start(0)
		self.greenPwr.start(0)

		# Dictionary to keep track of colors and RGB
		self.colors = {"blue":[0,0,256],
						"red":[256,0,0],
						"green":[0,256,0],
						"yellow":[255,255,0],
						"orange":[255,255,0],
						"purple":[138,43,226],
						"pink":[255,105,180],
						"springgreen":[0,255,127],
						"turquoise":[64,224,208],
						"off":[0,0,0],
						"white":[255,255,255]}

	def rgb_to_pct(self, rgb):
		"""
		Takes rgb from 0 to 256 and makes it 0 to 100 value
		"""
		return 100*rgb/256

	def update_light(self, color, val):
		"""
		Takes in a color (as a string) and a new RGB value
		"""
		col_map = {"red":self.redPwr, "green":self.greenPwr, "blue":self.bluePwr}
		if color not in list(col_map.keys()):
			raise ValueError("Please choose a valide color to change")
		else:
			col = col_map[color]
			new = float(val)
			col.ChangeDutyCycle(new)

	def change_color(self, cmd):
		"""
		changes light color according to the command
		"""
		# get color code
		rgb = self.colors[cmd]
		
		# map to duties
		duty = [self.rgb_to_pct(x) for x in rgb]
		
		self.update_light("red", duty[0])
		self.update_light("green", duty[1])
		self.update_light("blue", duty[2])
		print("color updated")

	def light_off(self):
		"""turns light off"""
		for c in ["red", "green", "blue"]:
			self.update_light(c, 0)
	
	def run_jump(self):
		self.kill = False # it is okay to jump now
		num_colors = len(self.colors.keys())
		keys = list(self.colors.keys())
		i = 0
		while not self.kill:
			color = keys[i]
			print("Trying to change color to", color)
			self.change_color(color)
			time.sleep(self.jump_pause)
			i = (i + 1)%num_colors
			
	def quit(self):
		self.kill = True
		self.light_off()
