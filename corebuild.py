""" 
Game core file : this file contains the mechanics of the game

McGyver game

Game in which McGyver must cross a labyrinth and defeat his guardian. Along the way, he must find a straw and a needle to make a sarbacanne.

I know, it looks crazy

Script : Python
Files : corebuild.py, classes.py, configuration.py images, sond and music.

"""

#import of pygame lib
import pygame
from pygame.locals import *

#import other files : classes and configuration
from classes import *
from constants import *

pygame.init()

#open a game window
window = pygame.display.set_mode((window_size, window_size))
#window icon
icon = pygame.image.load(img_icon)
pygame.display.set_icon(icon)

#title
pygame.display.set_caption(window_title)
continuer = 1

#main loop
while continuer:
    pygame.time.Clock().tick(30)
    continue