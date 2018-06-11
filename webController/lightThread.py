# lightThread.py
# Kenneth Lipke
# Summer 2018


"""
File contraining the lightThread class, a subclass of threading.Thread
This controlls all lights in a seperate thread, that can run in the 
background with Flask, so it can run on a constant loop and the program
can still take jquery updates
"""

class lightThread(threading.Thread):
	def __init__(self):
		# Main initializers
		threading.Thread.__init__(self)
		self.kill = False

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
						"turquoise":[64,224,208]}

	def rgb_to_pct(self, rgb):
		"""
		Takes rgb from 0 to 256 and makes it 0 to 100 value
		"""
		return 100*rgb/256

	def update_light(self, color, val):
		"""
		Takes in a color (as a string) and a new RGB value
		"""
		col_map = {"red", self.redPwr, "green":self.greenPwr, "blue":self.bluePwr}
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
		rgb = colors[cmd]
		
		# map to duties
		duty = [rgb_to_pct(x) for x in rgb]
		
		update_color("red", duty[0])
		update_color("green", duty[1])
		update_color("blue", duty[2])
		print("color updated")

	def light_off():
		"""turns light off"""
		for c in ["red", "green", "blue"]:
			self.update_color(c, 0)
	
	def run_jump(self):
		num_colors = len(colors.keys())
		keys = list(colors.keys())
		i = 0
		while not self.kill:
			color = keys[i]
			print("Trying to change color to", color)
			change_color(color)
			time.sleep(0.5)
			i = (i + 1)%num_colors
			
	def quit(self):
		self.kill = True
		self.light_off()