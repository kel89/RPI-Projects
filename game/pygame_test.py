# pygame test

import pygame 
from pygame.locals import *
import sys
import random

pygame.init() # initialize pygame

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height)) # internalizing window with size
screen.fill((255, 255, 255)) # setting a fill color
pygame.display.set_caption("Raspberry Catching game") # window caption

class Spoon:
	
	def __init__(self, screen, x_start, y_start):
		self.x = x_start
		self.y = y_start
		self.image = pygame.image.load("spoon.jpg").convert()
		self.screen= screen
		
	def set_coords(self,x,y):
		self.x = x
		self.y = y
		
	def get_coords(self):
		return self.x, self.y
		
	def update(self):
		x,y = pygame.mouse.get_pos()
		self.set_coords(x,y)
		#screen.blit(self.image, (self.x, self.y))
		self.screen.blit(self.image, (self.x, self.y))
		
class Raspberry:
	
	def __init__(self, screen, x_start=None, y_start=None):
		if x_start == None and y_start == None:
			# set random start
			x_start = random.randint(0, screen_width)
			y_start = 0		
		
		self.x = x_start
		self.y = y_start
		self.screen = screen
		self.image = ball = pygame.image.load("raspberry.jpg").convert()
		
	def set_coords(self,x,y):
		self.x = x
		self.y = y
		
	def get_coords(self):
		return self.x, self.y
		
	def update(self):
		"""makes it fall"""
		self.set_coords(self.x + random.randint(-1, 1), self.y +.1)
		self.screen.blit(self.image, (self.x, self.y))
		

# Initialize spoon class
spoon = Spoon(screen, 300, 300)
berry1 = Raspberry(screen)

while True:
	
	# create quit option
	for event in pygame.event.get():
		if event.type== QUIT:
			sys.exit()
			
	# Draw update
	screen.fill((255, 255, 255))
	spoon.update()
	berry1.update()
	
	pygame.display.update()

