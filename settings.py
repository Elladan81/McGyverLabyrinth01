""" 

My constant file contains the addresses of the images, for an easier modification, 
the title of the window, its icon, the number of sprites on a width, the size of the sprites, 
and therefore the size of the window (multiplies the last two constants ) 

"""


class Settings:

    def __init__(self):
        # window setting
        self.num_sprite_len = 15
        self.sprite_size = 30
        self.window_height = (self.num_sprite_len + 1) * self.sprite_size
        self.window_width = self.num_sprite_len * self.sprite_size

        # window configuration
        self.window_title = "McGyver Labyrinthe"
        self.img_icon = "images/MacGyver.png"

        # game picture
        self.img_macgyver = "images/macgyver.png"
        self.img_home = "images/home.png"
        self.img_background = "images/background.png"
        self.img_wall = "images/wall.png"
        self.img_finish = "images/finish.png"
        self.img_needle = "images/items/needle.png"
        self.img_straw = "images/items/straw.png"
        self.img_ether = "images/items/ether.png"
