"""
classes will be here

this file will contain classes :

Level : with two methods, one that generates a level from one file in a structure attribute, the other that displays it on the screen

Character : who creates a character, with a position, a current image (current direction), a position in a box, a position in pixels ...
It contains only one method, that of displacement.
It also recovers the structure of the level, to know the type of each box, and to prevent the displacement if it is a wall. 

Items to collect : creates item with a random position, a current image, how to collect item, item count and condition
"""

import pygame
from pygame.locals import *
from constantes import *

class Level:
    """this class creates the lvl"""
    def __init__(self,file1):
        self.file1 = file1
        self.structure = 0
    
    def generate(self):
        """method generates the lvl with the file. Create a list, containing a list per lines"""
        #open file
        with open(self.file1, "r") as file1:
            structure_lvl = []
        #read file
        for line in file1:
            line_lvl= []
            for sprite in line:
                if sprite != '\n':
                    line_lvl.append(sprite)
            structure_lvl.append(line_lvl)
        self.structure = structure_lvl
    
    def afficher(self, window):
        wall = pygame.image.load(img_wall).convert()
        start = pygame.image.load(img_start).convert()
        finish = pygame.image.load(img_finish).convert_alpha()

    num_line = 0
    for line in self.strucutre:
        num_case = 0
        for sprite in line:
            x = num_case*sprite_size
            y = num_line*sprite_size
            if sprite =='m':
                window.blit(wall, (x,y))
            elif sprite =='s':
                window.blit(start, (x,y))
            elif sprite =='f':
                window.blit(finish, (x,y))
            num_case += 1
        num_line +=1

class MacGuyver:
    def __init__(self, right, left, up, down, Level):
        #charachter sprite
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image_load(up).convert_alpha()
        self.down = pygame.image_load(down).convert_alpha()
        #character position
        slef.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y =0
        #start Direction
        slef.direction = self.right
        #lvl start
        self.level = Level
    
    def move(self, direction):
        """method to move the character"""
        #move
        if direction == 'right':
            #to not leave the labyrinth
            if self.case_x < (num_sprite_len -1):
                #we chack that is not a wall
                if self.level.strucutre[self.case_y][self.case_x+1] != 'm':
                    #move one step
                    slef.case_x +=1
                    #calculate real position in pixel
                    self.x = self.case_x*sprite_size
            #img in the good position
            self.direction = self.right
        #move left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.strucutre[self.case_y][self.case_x-1] != 'm':
                    slef.case_x -=1
                    self.x = self.case_x*sprite_size
            self.direction = self.left
        #move top
        if direction == 'up':
            if self.case_x > 0:
                if self.level.strucutre[self.case_y-1][self.case_x] != 'm':
                    slef.case_y -=1
                    self.x = self.case_x*sprite_size
            self.direction = self.up
            #move down
        if direction == 'down':
            if self.case_y < (num_sprite_len -1):
                if self.level.strucutre[self.case_y+1][self.case_x] != 'm':
                    slef.case_y +=1
                    self.x = self.case_x*sprite_size
            self.direction = self.down