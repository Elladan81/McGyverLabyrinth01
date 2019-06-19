""" 
Game core file : this file contains the mechanics of the game

McGyver game

Game in which McGyver must cross a labyrinth and defeat his guardian. Along the way, he must find a straw and a needle to make a sarbacanne.

I know, it looks crazy

Script : Python
Files : corebuild.py, classes.py, configuration.py images, sond and music.

"""

# import of pygame lib
import pygame
from pygame.locals import *

# import other files : classes and configuration
from classes import *
from settings import *

pygame.init()

# open a game window
window = pygame.display.set_mode((window_size, 480))
# window icon
icon = pygame.image.load(img_icon)
pygame.display.set_icon(icon)

# title
pygame.display.set_caption(window_title)


# Main start victory condition
StrawPicked = False
NeedlePicked = False
EtherPIcked = False
YOU_WIN = False
YOU_LOOSE = False

# Main Loop
continue_main = 1

pygame.key.set_repeat(400,30) # moving MacGyver by maintening a key

while continue_main:
    # load Home screen
    home = pygame.image.load(img_home).convert()
    window.blit(home, (0,0))
    pygame.display.flip()

    continue_game = 1
    continue_home = 1

    # Home loop
    while continue_home:
        # limit refreshing screen loop
        pygame.time.Clock().tick(30)

        # if user quit, the game is over
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_home = 0
                continue_game = 0
                continue_main = 0
                choose = 0
            
            elif event.type == KEYDOWN:
                #lauch 1st lvl
                if event.key == K_RETURN:
                    continue_home = 0
                    choose = 'lvl1'
    # check player choose a lvl, to not laod if leave
    if choose != 0:
        #load images
        background = pygame.image.load(img_background).convert()
        window.blit(background, (0,30))

        level = Level(choose)
        level.generate()
        level.afficher(window)

        mg = MacGyver(img_macgyver, level)
        straw = Stuff(img_straw, level)
        straw.display_item(img_straw, window)
        needle = Stuff(img_needle, level)
        needle.display_item(img_needle, window)
        ether = Stuff(img_ether, level)
        ether.display_item(img_ether, window)

    # Game Loop
    while continue_game:
        #limite game loop
        pygame.time.Clock().tick(30)
    	# if user quit = var = 0 to close the window
        for event in pygame.event.get():
            if event.type == QUIT:
                continue_game = 0
                continue_main = 0
            elif event.type == KEYDOWN :
                if event.type == K_ESCAPE:
                    continue_game = 0
                # key to move MacGyver
                elif event.key == K_RIGHT:
                    mg.move('right')
                elif event.key == K_LEFT:
                    mg.move('left')
                elif event.key == K_UP:
                    mg.move('up')
                elif event.key == K_DOWN:
                    mg.move('down')

        #display at new positions
        window.blit(background, (0,30))
        level.afficher(window)
        window.blit(mg.direction, (mg.x, mg.y))

        if StrawPicked is False:
            window.blit(straw.strawimage, (straw.x, straw.y))
        if (mg.x, mg.y) == (straw.x, straw.y):
            StrawPicked = True
            window.blit(straw.strawimage, (10,0))

        if NeedlePicked is False:
            window.blit(needle.needleimage, (needle.x, needle.y))
        if (mg.x, mg.y) == (needle.x,needle.y):
            NeedlePicked = True
            window.blit(needle.needleimage, (50,0))

        if EtherPIcked is False:
            window.blit(ether.etherimage, (ether.x, ether.y))
        if (mg.x, mg.y) == (ether.x, ether.y):
            EtherPIcked = True
            window.blit(ether.etherimage, (90,0))


        pygame.display.flip()

        #end game (without condition)
        if level.structure[mg.case_y][mg.case_x] == 'f':
            # If MacGyver reach the guard :
            if StrawPicked is True and NeedlePicked is True and EtherPIcked is True:  # If every objects have been looted, it's ok, you win !
                YOU_WIN = True
            else:
                YOU_LOOSE = True  # Else it's game over ! You loose !
            
        # create a final scene, with a text in the middle of the screen
        if YOU_WIN is True:
            window.blit(background, (0, 30))  # draw over everything on the screen now by re-drawing the background
            font = pygame.font.Font(None, 25)
            text = font.render("You won ! MacGyver escaped from this deadly trap !", 1, (255, 255, 255)) # Display the text in white with rounded edge
            textrect = text.get_rect()
            textrect.centerx, textrect.centery = window_size / 2, window_size / 2  # Centering the text 
            window.blit(text, textrect)

            pygame.display.flip()

        if YOU_LOOSE is True:
            window.blit(background, (0, 30))  # draw over everything on the screen now by re-drawing the background
            font = pygame.font.Font(None, 25)
            text = font.render("Murdoc caught you. It's over for you, McGyver !.", 1, (255, 255, 255))  # Display the text in white with rounded edge
            textrect = text.get_rect()
            textrect.centerx, textrect.centery = window_size / 2, window_size / 2
            window.blit(text, textrect)

            pygame.display.flip()