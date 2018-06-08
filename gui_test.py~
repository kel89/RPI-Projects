from Tkinter import *

def hello_world():
	root = Tk()
	Label(root, text="Hello World").pack()
	root.mainloop()
	
def set_window_start(root):
	"""sets where the window will open"""
	ws = root.winfo_screenwidth() # gets width of screen
	hw = root.winfo_screenheight() # gets height of screen
	
	# I want it to open in the bottom left
	x = 3.0*ws/4
	y = ws/4.0
	
	# set (width, height, x, y)
	root.geometry( '%dx%d+%d+%d' % (300, 230, x, y) ) 

class Temp_App:
	"""Class for temperature converter app. Master is the window from Tkinter."""
	
	def __init__(self, master):
		"""requires that you feed it the Tkinter window root window"""		
		# define fields -- These are special Tkinter variable types
		self.c = DoubleVar()
		self.f = DoubleVar() 
		self.result = DoubleVar()	
		self.comment=StringVar()
		self.radio_value = StringVar()
		self.radio_value.set("N")
				
		# set Frame for app and "pack" it
		frame = Frame(master)
		frame.pack()
		
		#place labels, entries, and button
		self.place_labels(frame)
		self.place_entries(frame)
		self.place_buttons(frame)
		
		# Test spinbox
		#Spinbox(frame, values=("a", "b", "c")).grid(row=3, column=0, columnspan=2)
		
		# Radio Button
		Radiobutton(frame, text="F to C", variable=self.radio_value, value="F").grid(row=5, column=0)
		Radiobutton(frame, text="C to F", variable=self.radio_value, value="C").grid(row=5, column=1)

	def place_labels(self, frame):
		Label(frame, text="deg C").grid(row=0, column=0) # C label
		Label(frame, text="deg F").grid(row=1, column=0)	 # F label
		#Label(frame, textvariable=self.f).grid(row=1, column=1) # the number for F
		#Label(frame, textvariable=self.result).grid(row=3, column=0, columnspan=2) # Tag the result

		# add the comment label at bottom
		Label(frame, textvariable=self.comment).grid(row=4, column=0, columnspan=2)
		
		
	def place_entries(self, frame):
		Entry(frame, textvariable=self.c).grid(row=0, column=1)
		Entry(frame, textvariable=self.f).grid(row=1, column=1)
		
	def place_buttons(self, frame):
		button = Button(frame, text="Convert", command=self.convert) # button calls the convert method
		button.grid(row=2, column=0, columnspan=2)
			
	def convert(self):
		radio_value = self.radio_value.get()
		if radio_value == "N":
			self.comment.set("Please Select a Conversion Direction")
			return
		
		elif radio_value == "C":
			c = self.c.get()		
			f = c*(9.0/5.0) + 32
			if f < 32:
				self.comment.set("Brr")
			else:
				self.comment.set("Nice")
			self.f.set(f)
		
		else:
			f = self.f.get()
			c = (f-32)*5.0/9
			self.c.set(c)			


def temp_app_start():
	root = Tk()
	set_window_start(root) # sets where the window will open
	root.wm_title("Temp Converter")
	app = Temp_App(root)
	root.mainloop()

if __name__ == "__main__":
	#hello_world()
	temp_app_start()
	