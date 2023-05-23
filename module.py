import pygame as py
import random
import time
from pygame.sprite import Sprite
from constants import *
#from racing import score



class Player(Sprite):
    GRAVITY = 5
    player_group = py.sprite.Group()
    def __init__(self, player_name, color, width, height, x_axis, y_axis, speed=0):

        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(color)

        self.rect.x = x_axis
        self.rect.y = y_axis

        self.speed = speed
        self.mass = 20
        self.fall_count = 1
        self.jump_force = 10
        
        self.player_name = player_name

        Player.player_group.add(self)

    
    def gravity(self):
        self.rect.y += int((self.fall_count / FPS) * self.GRAVITY)
        self.fall_count += 1


    def update(self):
        self.gravity()




def create_player(player_name, color, width, height, x, y):
    player = Player(player_name, color, width, height, x, y)



class Platforms(Sprite):
    platform_group = py.sprite.Group()
    def __init__(self, color, width, height, x_axis, y_axis):

        py.sprite.Sprite.__init__(self)
        self.image = py.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(color)

        self.rect.x = x_axis
        self.rect.y = y_axis
    
        Platforms.platform_group.add(self)

def create_platform(color, width, height, x, y):
    platform = Platforms(color, width, height, x, y)