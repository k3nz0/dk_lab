#!/usr/bin/python2 
# coding : utf-8

# k3nz0, 23/01/2013
# This is my first project with pygame , trying it was really a good idea. 
# For reporting bugs, giving suggestions or what else ever, feel free to contact me via e-mail
# Here it is : k3nz09p[at]gmail[dot]com

import pygame
from pygame.locals import *
from classes import *
from constants import *
import time

pygame.init()
pygame.time.Clock().tick(30)
window = pygame.display.set_mode(size)

pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

menu_bg = pygame.image.load(welcome).convert()
begin = pygame.image.load(begin).convert()
end = pygame.image.load(end).convert_alpha()
wall = pygame.image.load(wall).convert()
game_bg = pygame.image.load(background).convert()
win = pygame.image.load(win).convert()


dk = []
dk.append(pygame.image.load(dk_down).convert_alpha())
dk.append(pygame.image.load(dk_up).convert_alpha())
dk.append(pygame.image.load(dk_right).convert_alpha())
dk.append(pygame.image.load(dk_left).convert_alpha())
# dk[0] : down
# dk[1] : up
# dk[2] : right
# dk[3] : left

cmon_menu=1
cmon_game=0

while 1:
	while cmon_menu: # Menu loop, waiting for the level's choice
		window.blit(menu_bg, (0,0))
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_F1:
				cmon_menu=0
				cmon_game=1
				level = 'level1'
				break
			if event.type == KEYDOWN and event.key == K_F2:
				cmon_menu=0
				cmon_game=1
				level = 'level2'
				break
			if event.type == QUIT:
				exit(0)

		pygame.display.flip()
	
	first_time=1
	
	#Game loop, type "$" to break it :>!
	while cmon_game:
		window.blit(game_bg, (0,0))
		tapz= Niveau()
		tapz.generate_level(level)
		tapz.print_level(tapz.list_level, window, begin, wall, end)
		if first_time==1:
			monster = Perso(dk, tapz.list_level)
			first_time=0
		if monster.win==1:
			window.blit(win, (20,20))
			pygame.display.flip()
			time.sleep(3)
			cmon_game=0
			cmon_menu=1
		# dk[0] : down
		# dk[1] : up
		# dk[2] : right
		# dk[3] : left
		if monster.last_movement == "down":
			window.blit(dk[0], monster.position_rect)
		elif monster.last_movement == "up":
			window.blit(dk[1], monster.position_rect)
		elif monster.last_movement == "right":
			window.blit(dk[2], monster.position_rect)
		elif monster.last_movement == "left":
			window.blit(dk[3], monster.position_rect)
		

		for event in pygame.event.get():
			# Back to menu when typing "$"
			if event.type == KEYDOWN and event.key == K_DOLLAR:
				cmon_game=0
				cmon_menu=1
				break
			if event.type == KEYDOWN and event.key == K_LEFT:
				monster.move_perso(monster.position_rect, tapz.list_level, "left")
			if event.type == KEYDOWN and event.key == K_RIGHT:
				monster.move_perso(monster.position_rect, tapz.list_level, "right")
			if event.type == KEYDOWN and event.key == K_DOWN:
				monster.move_perso(monster.position_rect, tapz.list_level, "down")
			if event.type == KEYDOWN and event.key == K_UP:
				monster.move_perso(monster.position_rect, tapz.list_level, "up")
			if event.type == QUIT:
				exit(0)

		pygame.display.flip()
# Done with love.
