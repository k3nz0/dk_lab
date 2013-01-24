#!/usr/bin/python2
# coding: utf-8

class Niveau:
	"""
		2 methods :
		 - Generate the level from the given file dans un attribut structure
		 - Print the level structure \o/
	"""
	def generate_level(self, fichier):
		"""
			-Generate the level structure from the given file
		"""
		fp = open("levels/"+fichier, 'r').read()
		list_level = fp.split('\n')
		# Remove the last \n
		list_level.pop()
		self.list_level = list_level
	def print_level(self, list_level, window, begin, wall, end):
		"""
			Method which aim is to print the level structure into the window
				- It will parse the given structure
				     "d" is departure box
				     "m" is the wall
				     "a" the end (the banana :D)
			position_x = num_case_x * sprite's length in pixels
			position_y = num_case_y * sprite's length in pixels
			 
		"""
		for y in range(0,15):
			for x in range(0,15):
				if list_level[y][x] == 'd':
					position_x = x * 30
					position_y = y * 30
					window.blit(begin, (position_x,position_y))
				elif list_level[y][x] == 'm':
					position_x = x * 30
					position_y = y * 30
					window.blit(wall, (position_x,position_y))
				elif list_level[y][x] == 'a':
					position_x = x * 30
					position_y = y * 30
					window.blit(end, (position_x,position_y))
				else: # it's a 0
					continue
		

class Perso:
	
	"""
	Create a character, and define; 
	     * position ( in both boxes and pixels)
	     * image (default image is down)
	"""
	def __init__(self, dk, list_level):
		class Found(Exception): pass
		try:
			for y in range(0,15):
				for x in range(0,15):
					if list_level[y][x]=='d':
						raise Found
		except Found:
			self.position = (x*30, y*30)
			self.position_case = (x,y)
		# Display dk down (default value)
		self.position_rect = dk[0].get_rect()
		self.position_rect.left= self.position[0]
		self.position_rect.top = self.position[1]
		# default value
		self.last_movement="down"
		self.win=0

	def move_perso(self, position_rect, list_level, movement):
		"""
		Method which aim is to move the character:
			The "m" represents the wall, we (unfortunately ) are not allowed to walk into walls :d
		"""
		#pixels
		pos_x = position_rect.left
		pos_y = position_rect.top

		#boxes
		x = (pos_x / 30)
		y = (pos_y / 30)

		self.last_movement = movement

		#Uncomment these lines, only for debugging purposes
		#print x, y
		#print list_level[y][x-1]
		
		#left
		if movement == "left" and (x-1)>=0:
			if list_level[y][x-1]=='0' or list_level[y][x-1]=='d':
				self.position_rect = position_rect.move(-30, 0)
			elif list_level[y][x-1]=='a':
				self.position_rect = position_rect.move(-30, 0)
				self.win=1
				#print "You win!"
		#right
		elif movement == "right" and (x+1)<15:
			if list_level[y][x+1]=='0' or list_level[y][x+1]=='d':
				self.position_rect = position_rect.move(30,0)
			elif list_level[y][x+1]=='a':
				self.position_rect = position_rect.move(30,0)
				self.win=1
				#print "You win!"
		#down
		elif movement == "down" and (y+1)<15:
			if list_level[y+1][x] == '0' or list_level[y+1][x]=='d':
				self.position_rect = position_rect.move(0,30)
			elif list_level[y+1][x]=='a':
				self.position_rect = position_rect.move(0,30)
				self.win=1
				#print "You win!"
		#up
		elif movement == "up" and (y-1)>=0:
			if list_level[y-1][x] == '0' or list_level[y-1][x]=='d':
				self.position_rect = position_rect.move(0,-30)
			elif list_level[y-1][x]=='a':
				self.position_rect = position_rect.move(0,-30)
				self.win=1
				#print "You win!"

		#else:
		#		print "owned, nothin"