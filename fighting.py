import pygame as py 
import time
import random

from constants import *
from module import *

py.init()

screen = py.display.set_mode((WIDTH, HEIGHT))


#Create player
create_player("Kirbo", PINK, 20, 20, 400, 0)

# create platforms
main_platform = create_platform(RED, 400, 50, 300, 400)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    clock.tick(FPS)


    # Update
    py.display.update()
    Platforms.platform_group.update()
    Player.player_group.update()

    # Draws background
    screen.fill(BACKGROUND)

    # Draw 
    Platforms.platform_group.draw(screen)
    Player.player_group.draw(screen)
    