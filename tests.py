#!/usr/bin/python2 
# -*-coding : utf-8 -*-

fp = open('level1', 'r').read()
list_level = fp.split('\n')
list_level.pop()

class Perso:
	def __init__(self, list_level):
		class Found(Exception): pass
		try:
			for y in range(0,15):
						for x in range(0,15):
							if list_level[y][x]=='d':
								raise Found
		except Found:
			self.position = (x*30, y*30)
			print self.position

tapz = Perso(list_level)

def __init__(self, window, dk, list_level):
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
		window.blit(dk[0], self.position_rect)