"""
classes will be here

this fichier will contain classes :

Level : with two methods, one that generates a level from one fichier in a structure attribute, the other that displays it on the screen

Character : who creates a character, with a position, a current image (current direction), a position in a box, a position in pixels ...
It contains only one method, that of displacement.
It also recovers the structure of the level, to know the type of each box, and to prevent the displacement if it is a wall. 

Items to collect : creates item with a random position, a current image, how to collect item, item count and condition
"""

import pygame
import random
from pygame.locals import *
from constants import *

class Level:
    """this class creates the lvl"""
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        self.wall = pygame.image.load(img_wall).convert()
        self.start = pygame.image.load(img_start).convert()
        self.finish = pygame.image.load(img_finish).convert()
    
    def generate(self):
        """method generates the lvl with the file. Create a list, containing a list per lines"""
        #open file
        with open(self.fichier, "r") as fichier:
            structure_lvl = []
            #read fichier
            for line in fichier:
                line_lvl= []
                for sprite in line:
                    if sprite != '\n':
                        line_lvl.append(sprite)
                structure_lvl.append(line_lvl)
            self.structure = structure_lvl
    
    def display_level(self, window):

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case*sprite_size
                y = num_line*sprite_size
                if sprite =='m':
                    window.blit(self.wall, (x,y))
                elif sprite =='s':
                    window.blit(self.start, (x,y))
                elif sprite =='f':
                    window.blit(self.finish, (x,y))
                num_case += 1
            num_line +=1

class MacGyver:
    def __init__(self, mgimage, Level):
        #  charachter sprite
        self.mgimage = pygame.image.load(img_macgyver).convert_alpha()
        # character position
        self.case_x = 0
        self.case_y = 1
        self.x = 0
        self.y =30
        self.direction = self.mgimage
        # lvl start
        self.level = Level
    
    def move(self, direction):
        """method to move the character"""
        # move right
        if direction == 'right':
            # to not leave the labyrinth
            if self.case_x < (num_sprite_len -1):
                #we chack that is not a wall
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    # move one step
                    self.case_x +=1
                    # calculate real position in pixel
                    self.x = self.case_x*sprite_size
                   
        # move left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -=1
                    self.x = self.case_x*sprite_size

        # move top
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    if self.level.structure[self.case_y-1][self.case_x] != 'v':
                        self.case_y -=1
                        self.y = self.case_y*sprite_size
 
        # move down
        if direction == 'down':
            if self.case_y < (num_sprite_len):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y +=1
                    self.y = self.case_y*sprite_size


class Stuff:
    """this class create stuff can use to escape the maze"""
    def __init__(self, lootimage, Level):
        self.lootimage = lootimage
        self.strawimage = pygame.image.load(img_straw).convert_alpha()
        self.needleimage = pygame.image.load(img_needle).convert_alpha()
        self.etherimage = pygame.image.load(img_ether).convert_alpha()
        # item position
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.level = Level
        self.loaded = True

    def display_item(self, lootimage, window):
        # generate random position of the item
        while self.loaded:
            self.case_x = random.randint(0, 14)  # We randomize the case_x position
            self.case_y = random.randint(0, 14)  # same for case_y position
            if self.level.structure[self.case_y][self.case_x] == '0': # if the randomized position is located on a free space
                self.y = self.case_y * sprite_size  # We define/accept the position for the object
                self.x = self.case_x * sprite_size
                self.loaded = False  # Once we have defined a position for one object, the script is over
