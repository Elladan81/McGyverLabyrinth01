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
import classes import *
import configuration import *

pygame.init()

#open a game window
window = pygame.display.set_mode((640, 480))
#icon
icone = pygame.image.laod(image_icone)
pygame.display.set_icon(icone)
#titre
pygame.display.set_caption(title, icontitle=McGyver)