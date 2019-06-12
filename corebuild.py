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


#main loop

continuer = 1

while continuer:
    #load home screen
    home = pygame.image.load(img_home).convert()
    window.blit(home, (0,0))
    pygame.display.flip()

    continuer_game = 1
    continuer_home = 1
    #Home loop
    while continuer_home:
        #limit loop
        pygame.time.Clock().tick(30)

        #if user quit, the game is over
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_home = 0
                continuer_game = 0
                continuer = 0
                choix = 0
            
            elif event.type == KEYDOWN:
                #lauch 1st lvl
                if event.key == K_F1:
                    continuer_home = 0
                    choose = 'lvl1'
    #check player choose a lvl, to not laod if leave
    if choose !=0:
        background = pygame.image.load(img_background).convert()

        level = Level(choose)
        level.generate()
        level.afficher(window)

        mg = MacGuyver("images/MacGuyver.png", level)
    
    #Game Loop
    while continuer_game:
        #limite game loop
        pygame.time.Clock().tick(30)
    	#if user quit = var = 0 to close the window
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer_game = 0
                continuer = 0
            elif event.type == KEYDOWN :
                if event.type == K_ESCAPE:
                    continuer_jeu = 0
                #key to move MacGuyver
                elif event.key == K_RIGHT:
                    mg.move('right')
                elif event.key == K_LEFT:
                    mg.move('left')
                elif event.key == K_UP:
                    mg.move('up')
                elif event.key == K_DOWN:
                    mg.move('down')

        #display at new positions
        window.blit(background, (0,0))
        level.afficher(window)
        window.blit(mg.direction, (mg.x, mg.y))
        pygame.display.flip()

        #end game (without condition)
        if level.structure[mg.case_y][mg.case_x] == 'f':
            continuer_game = 0
