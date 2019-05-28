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

pygame.init()

#open a game window
window = pygame.display.set_mode((640, 480))

continuer = 1

while continuer:
    continuer