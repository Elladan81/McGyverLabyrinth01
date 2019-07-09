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


class MacGyverGame():
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resssource"""
        pygame.init()

        self.settings = Settings()
        self.window = pygame.display.set_mode(
            (self.settings.window_width, self.settings.window_height))  # open a game window
        self.icon = pygame.image.load(self.settings.img_icon)
        pygame.display.set_icon(self.icon)  # window icon
        pygame.display.set_caption(self.settings.window_title)  # title
        pygame.key.set_repeat(300, 30)  # support repeated key support

    def run_game(self):
        """main loop"""
        self.continue_main = True

        while self.continue_main:
            # load Home screen
            self._display_home_menu()

            pygame.display.flip()

            # Home loop
            while self.continue_home:
                # limit refreshing screen loop
                pygame.time.Clock().tick(30)

                self._check_home_keydown_event()

            # check player choose a lvl
            if self.choose != 0:

                self._display_background()
                self._generate_level()
                self._generate_initial_stuff()
                self._initiate_victory_condition()

            # Game Loop
            while self.continue_game:

                pygame.time.Clock().tick(30)

                self._check_game_keydown_event()
                self._display_background()
                self.level.display_level(self.window)
                self.mg.blitmg(self.window)
                self._update_item_position()
                self._check_victory_condition()

                pygame.display.flip()

    def _generate_level(self):
        # generate and display the level
        self.level = Level(self.choose)
        self.level.generate()
        self.level.display_level(self.window)

    def _generate_initial_stuff(self):
        # instantiate items and character
        self.mg = MacGyver(self.level)
        self.straw = Stuff(self.level, self.settings.img_straw)
        self.straw.display_item()
        self.needle = Stuff(self.level, self.settings.img_needle)
        self.needle.display_item()
        self.ether = Stuff(self.level, self.settings.img_ether)
        self.ether.display_item()

    def _display_background(self):
        # load background image
        background = pygame.image.load(self.settings.img_background).convert()
        self.window.blit(background, (0, 30))

    def _display_home_menu(self):
        # display home menu
        self.home = pygame.image.load(self.settings.img_home).convert()
        self.window.blit(self.home, (0, 0))
        self.continue_game = True
        self.continue_home = True

    def _initiate_victory_condition(self):
        # initiate main victory condition
        self.StrawPicked = False
        self.NeedlePicked = False
        self.EtherPicked = False

    def _check_home_keydown_event(self):
        """check user event on home menu"""
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.continue_home = False
                self.continue_game = False
                self.continue_main = False
                self.choose = 0

            elif event.type == KEYDOWN:  # launch random lvl
                if event.key == K_RETURN:
                    self.continue_home = False
                    list_level = ['lvl1', 'lvl2']  # list of level files
                    # choose a random level from the list
                    self.choose = random.choice(list_level)

    def _check_game_keydown_event(self):
        """check user event in game"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.continue_game = False
                self.continue_main = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.continue_game = False
                # key to move MacGyver
                elif event.key == K_RIGHT:
                    self.mg.move('right')
                elif event.key == K_LEFT:
                    self.mg.move('left')
                elif event.key == K_UP:
                    self.mg.move('up')
                elif event.key == K_DOWN:
                    self.mg.move('down')

    def _update_item_position(self):
        """update position of items on the screen"""

        font = pygame.font.Font(None, 25)
        item_text = font.render(
            "Item picked up :", 1, (255, 255, 255))
        textrect = item_text.get_rect()
        textrect.x, textrect.y = 10, 0
        self.window.blit(item_text, textrect)

        if self.StrawPicked is False:
            self.window.blit(self.straw.stuff_image,
                             (self.straw.x, self.straw.y))
        if (self.mg.x, self.mg.y) == (self.straw.x, self.straw.y):
            self.StrawPicked = True
            self.window.blit(self.straw.stuff_image,
                             (150, 0))

        if self.NeedlePicked is False:
            self.window.blit(self.needle.stuff_image,
                             (self.needle.x, self.needle.y))
        if (self.mg.x, self.mg.y) == (self.needle.x, self.needle.y):
            self.NeedlePicked = True
            self.window.blit(self.needle.stuff_image,
                             (190, 0))

        if self.EtherPicked is False:
            self.window.blit(self.ether.stuff_image,
                             (self.ether.x, self.ether.y))
        if (self.mg.x, self.mg.y) == (self.ether.x, self.ether.y):
            self.EtherPicked = True
            self.window.blit(self.ether.stuff_image, (230, 0))

    def _check_victory_condition(self):
        """check victory conditions if the player arrives at the gardian"""

        if self.level.structure[self.mg.case_y][self.mg.case_x] == 'f':
            # If MacGyver reach the guard :
            # If every objects have been looted, it's ok, you win !
            if self.StrawPicked and self.NeedlePicked and self.EtherPicked:
                # create a final scene, with a text in the middle of the screen
                self.window.fill((0, 0, 0))
                font = pygame.font.Font(None, 25)
                # Display text in white with rounded edge
                text = font.render(
                    "You won ! MacGyver escaped from this deadly trap !", 1, (255, 255, 255))
                textrect = text.get_rect()
                textrect.centerx, textrect.centery = self.settings.window_width / \
                    2, self.settings.window_height / 2  # Centering the text
                self.window.blit(text, textrect)

            else:  # Else it's game over ! You loose !
                self.window.fill((0, 0, 0))
                font = pygame.font.Font(None, 25)
                text = font.render(
                    "Murdoc caught you. It's over for you, McGyver !", 1, (255, 255, 255))
                textrect = text.get_rect()
                textrect.centerx, textrect.centery = self.settings.window_width / \
                    2, self.settings.window_height / 2
                self.window.blit(text, textrect)


if __name__ == "__main__":
    # make a game instance and run
    mg_game = MacGyverGame()
    mg_game.run_game()
