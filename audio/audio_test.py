# audio_test.py

import pyaudio
import numpy as np

import RPi.GPIO as GPIO
import time
import random


def audio_setup(CHUNK, RATE, FORMAT):
	"""Setup for pyaudio object and the audio stream
	returns: 	p -- the PyAudio object
						stream -- the audio stream part of the pyaudio object """

	p = pyaudio.PyAudio()
	stream = p.open(	format = FORMAT,
												channels=1,
												rate = RATE,
												input=True, # uses default audio input
												frames_per_buffer = CHUNK)
												
	return p, stream
	

def light_setup(RPIN, GPIN, BPIN):
	"""Takes in the pin locations for the 3 colors and initializes the GPIO
	returns; redPwr -- GPIO object for red color power
						greenPwr -- GPIO object for green
						bluePwr -- GPIO object for blue color"""
						
	# Setup GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RPIN, GPIO.OUT)
	GPIO.setup(GPIN, GPIO.OUT)
	GPIO.setup(BPIN, GPIO.OUT)
	
	redPwr = GPIO.PWM(RPIN, 500)
	bluePwr = GPIO.PWM(BPIN, 500)
	greenPwr = GPIO.PWM(GPIN, 500)
	
	print("Setting Initial Light")
	redPwr.start(0)
	bluePwr.start(0)
	greenPwr.start(0)
	
	return redPwr, greenPwr, bluePwr


	

if __name__ == "__main__":
	# Set Constants
	CHUNK = 2**11 # number of data points to read at a time
	RATE = 48000 # time resolution of recording (device-Hz)
	FORMAT = pyaudio.paInt16
	
	RPIN = 17
	GPIN = 22
	BPIN = 24
		
	p, stream = audio_setup(CHUNK, RATE, FORMAT)
	redPwr, greenPwr, bluePwr = light_setup(RPIN, GPIN, BPIN)
	
	redPwr.ChangeDutyCycle(50)
	toggle = True
	
	time = 2
	n = 50
	past_peaks = np.zeros([n])
	last_change = 0
	#for i in range(int(time*RATE/CHUNK)):
	for i in range(0,2):
		data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
		print(data.tolist())
		peak = np.average(np.abs(data))*2
		
		#if peak > np.mean(past_peaks) and abs(last_change - i) > 10:
		if peak>7200 and abs(last_change - i) > 3:
			last_change = i
			print("Changing")
			if toggle:
				redPwr.ChangeDutyCycle(100)
				toggle = False
			else:
				redPwr.ChangeDutyCycle(0)
				toggle = True
		past_peaks[i%n] = peak	
		
		bars = "#"*int(50*peak/2**16)
		print("%04d\t%05d\t%s"%(i, peak, bars))
		
	# close gently
	stream.stop_stream()
	stream.close()
	p.terminate()	
		
	
	
	