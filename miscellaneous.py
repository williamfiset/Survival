import pygame
from time import sleep, time

__author__ = 'William Fiset, Gabriel Antao'
__all__ = ['text_to_screen', 'display_health_bar', 'display_end_game_screen']

# Colors!
WHITE  = (255, 255, 255)
BLACK  = (0, 0 ,0)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)
YELLOW = (255, 255, 0)

# Make these constants?
health_bar_dark_img = pygame.image.load("images/other/health_bar_dark.png")
health_bar_light_img = pygame.image.load("images/other/health_bar_light.png")

end_of_game_display = pygame.image.load('images/dead.jpg')

"""
This function places text on the screen.
"""
def text_to_screen(screen, text, x, y, size = 15, color = WHITE, font_type = 'monospace'):
    try:

        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as exception:
        print('Font Error, saw it coming')
        raise exception


""" Updates the player's Health bar """
def display_health_bar(screen, survivor_health , SCREEN_WIDTH):
    
    screen.blit(health_bar_dark_img, (SCREEN_WIDTH / 2 - 50, 0))
    screen.blit(health_bar_light_img,(SCREEN_WIDTH / 2 - 50, 0), (0, 0, survivor_health/ 10 , 11))

    text_to_screen(screen, 'HP:', 270, 0, color = RED)

    if survivor_health < 150:
        color = YELLOW
    else:
        color = BLACK

    text_to_screen(screen, str(survivor_health), SCREEN_WIDTH / 2 - 10, 0, 10, color)



# Displays the 'zombies ate your brain credits'
def display_end_game_screen(screen, PAUSE_TIME):

    sleep(PAUSE_TIME)
    screen.blit(end_of_game_display, (0, 0))

    # Actually updates the screen
    pygame.display.update()



"""
The Timer class provides an easy way to calculate: code execution time.

Usage:

timer = Timer()
# Code to time
timer.stop()

"""

class Timer():

    def __init__(self):

        self.start_time = time()

    def stop(self, return_value = False):

        if return_value == False:
            print(time() - self.start_time)
        else:
            return (time() - self.start_time)



