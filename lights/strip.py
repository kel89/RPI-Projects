# Ken Lipke
# strip.py

import RPi.GPIO as GPIO
from tkinter import *
import time
import random


class StripApp:
	"""GUI for light strip control
	Fields:		redPwr: from 0 to 100 controls power of red light
						bluePwr: from 0 to 100 controls power of blue light
						greenPwr: from 0 to 100 controls power of green light
						
						running: boolean used to start and stop the dancing. it is set to True
											by default. When "off" is hit it goes to false, and when "on" is hit
											it goes to True. Therefore, after the first time, you must hit on before
											dance will work again.
						
	"""
	
	def __init__(self, master, RPIN, GPIN, BPIN):
		
		# Setup Lights
		self.lightSetup(RPIN, GPIN, BPIN)
		
		# Setup GUI
		self.frame = Frame(master)
		self.frame.pack()
		
		self.setWindow()
		
		# for interruptiuons
		self.running = True
		
		
	def lightSetup(self, RPIN, GPIN, BPIN):
		"""Setup for the GPIO components, and creates power fields"""
		# Setup GPIO
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(RPIN, GPIO.OUT)
		GPIO.setup(GPIN, GPIO.OUT)
		GPIO.setup(BPIN, GPIO.OUT)
		
		self.redPwr = GPIO.PWM(RPIN, 500)
		self.bluePwr = GPIO.PWM(BPIN, 500)
		self.greenPwr = GPIO.PWM(GPIN, 500)
		
		print("Setting Initial Light")
		self.redPwr.start(0)
		self.bluePwr.start(0)
		self.greenPwr.start(0)
		
	def turnOff(self):
		"""Turns off the lights"""
		self.running=False
		self.update_red(0)
		self.update_green(0)
		self.update_blue(0)
		
	def turnOn(self):
		"""Turns lights on"""
		self.running=True
		self.update_red(50)
		self.update_green(50)
		self.update_blue(50)		
		
		
	def setWindow(self):
		# On/Off Buttons
		on_button = Button(self.frame, text="On", command=self.turnOn)
		on_button.grid(row=1, column=1)
		off_button = Button(self.frame, text="Off", command=self.turnOff)
		off_button.grid(row=1,column=2)
		
		# Color Sliders
		# Red
		Label(self.frame, text="Red").grid(row=2, column=1)
		self.red_slider = Scale(self.frame, orient=HORIZONTAL,
				from_=0, to=100, command=self.update_red)
		self.red_slider.grid(row=2, column=2)
		self.red_slider.set(0)
		
		# Green
		Label(self.frame, text="Green").grid(row=3, column=1)
		self.green_slider = Scale(self.frame, orient=HORIZONTAL,
				from_=0, to=100, command=self.update_green)
		self.green_slider.grid(row=3, column=2)
		self.green_slider.set(0)
		
		# Blue
		Label(self.frame, text="Blue").grid(row=4, column=1)
		self.blue_slider = Scale(self.frame, orient=HORIZONTAL,
				from_=0, to=100, command=self.update_blue)
		self.blue_slider.grid(row=4, column=2)
		self.blue_slider.set(0)
			
		# Dance button
		dance = Button(self.frame, text="Dance", command=self.dance)
		dance.grid(row=5, columnspan=2)
		
	def dance(self):
		if self.running:
				r = random.randint(0,100)
				g = random.randint(0,100)
				b = random.randint(0,100)
				self.update_red(r)
				self.update_green(g)
				self.update_blue(b)
				self.frame.after(500, self.dance)
		
	def update_red(self, duty):
		self.redPwr.ChangeDutyCycle(float(duty))
		self.red_slider.set(duty)
		
	def update_green(self, duty):
		self.greenPwr.ChangeDutyCycle(float(duty))
		self.green_slider.set(duty)
		
	def update_blue(self, duty):
		self.bluePwr.ChangeDutyCycle(float(duty))
		self.blue_slider.set(duty)
	
	
	def shutdown(self):
		"""kills the lights for shutdown only"""
		print("\nShutting Down")
		self.redPwr.ChangeDutyCycle(0)
		self.greenPwr.ChangeDutyCycle(0)
		self.bluePwr.ChangeDutyCycle(0)
		time.sleep(0.01)
		
		
def set_window_start(root):
	"""sets where the window will open"""
	ws = root.winfo_screenwidth() # gets width of screen
	hw = root.winfo_screenheight() # gets height of screen
	
	# I want it to open in the bottom left
	x = 3.0*ws/4
	y = ws/3.0
	
	# set (width, height, x, y)
	root.geometry( '%dx%d+%d+%d' % (300, 300, x, y) ) 


if __name__ == "__main__":
	root = Tk()
	root.wm_title("Strip Controller")
	set_window_start(root)
	RPIN = 17
	GPIN = 22
	BPIN = 24
	app = StripApp(root, RPIN, GPIN, BPIN)
	try:
		root.mainloop()
	finally:
		app.shutdown()
		print("Cleaning Up")
		GPIO.cleanup()
		
		