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
import os
from pygame.locals import *
from settings import *


class Level:
    """this class creates the lvl"""

    def __init__(self, level_file):
        self.settings = Settings()
        self.level_file = level_file
        self.structure = 0
        self.wall = pygame.image.load(self.settings.img_wall).convert()
        self.finish = pygame.image.load(self.settings.img_finish).convert()

    def generate(self):
        """method generates the lvl with the level file. Create a list, containing a list per lines"""
        # open file
        with open(self.level_file, "r") as level_file:
            structure_lvl = []
            # read level_file
            for line in level_file:
                line_lvl = []
                for sprite in line:
                    if sprite != '\n':
                        line_lvl.append(sprite)
                structure_lvl.append(line_lvl)
            self.structure = structure_lvl

    def display_level(self, window):
        """ method to display the maze """
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case*self.settings.sprite_size
                y = num_line*self.settings.sprite_size
                if sprite == 'm':
                    window.blit(self.wall, (x, y))
                elif sprite == 'f':
                    window.blit(self.finish, (x, y))
                num_case += 1
            num_line += 1


class MacGyver():
    """this class create MacGuyver and add move and blit methods"""

    def __init__(self, level):
        #  charachter sprite
        self.settings = Settings()
        self.mgimage = pygame.image.load(
            self.settings.img_macgyver).convert_alpha()
        # character start position
        self.case_x = 0
        self.case_y = 1
        self.x = 0
        self.y = 30
        # lvl start
        self.level = level
        

    def move(self, direction):
        """method to move the character"""
        # move right
        if direction == 'right':
            # prevents from going out the labyrinth/screen
            if self.case_x < (self.settings.num_sprite_len - 1):
                # we check that the position is not a wall
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    # move one step
                    self.case_x += 1
                    # calculate real position in pixel
                    self.x = self.case_x*self.settings.sprite_size

        # move left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x*self.settings.sprite_size

        # move top
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    if self.level.structure[self.case_y-1][self.case_x] != 'v':
                        self.case_y -= 1
                        self.y = self.case_y*self.settings.sprite_size

        # move down
        if direction == 'down':
            if self.case_y < (self.settings.num_sprite_len):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y*self.settings.sprite_size

    def blitmg(self, window):
        window.blit(self.mgimage, (self.x, self.y))

class Stuff():
    """this class create stuff MacGyver can use to escape the maze"""

    def __init__(self, level, stuff_image):
        self.settings = Settings()
        self.stuff_image = pygame.image.load(stuff_image).convert()
        # item position
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.level = level
        self.loaded = True  # condition to display item
       
    def display_item(self):
        # generate random position of the item
        while self.loaded:
            # We randomize the case_x position
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)  # same for case_y position
            # if the randomized position is located on a free space
            if self.level.structure[self.case_y][self.case_x] == '0':
                # We define/accept the position of the object
                self.y = self.case_y * self.settings.sprite_size
                self.x = self.case_x * self.settings.sprite_size
                self.loaded = False  # Once we have defined the position of the object, the script is over
    