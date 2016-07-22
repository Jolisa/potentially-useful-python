import pygame
from pygame.locals import*
import random
#define some colors
black= (0,0,0)
white= (255,255,255)
red=(255,0,0)
green= (0,255,0)
purple=(70,0,200)
blue=(0,0,255)
grey=(127,127,127)
pygame.init()

#set width and height of screen
screen_width=700
screen_height=500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ball Game")
done=False
clock=pygame.time.Clock()
possible_ball_colors=[black,white,green, red, blue, grey]

class Snow():
    def __init__(self, x_location, y_location, x_speed,y_speed, flake_size):
        self.x_location=x_location
        self.y_location=y_location
        self.x_speed=x_speed
        self.y_speed=y_speed
        self.flake_size=flake_size
    def snowFall(self,screen,colors,screen_width, screen_height):
        if self.y_location>screen_height:
            self.y_location=0
        #pygame.draw.circle(screen,ball_color,[self.x_location, self.y_location],self.ball_size)
            
        
        
diffsnow=Snow(20,0,5,5,4)
#2_snow=(30,0,3,3,4)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(purple)
    diffsnow.snowFall(screen,possible_ball_colors[1],screen_width, screen_height)
    #2_snow.snowFall(screen,possible_ball_colors[1],screen_width, screen_height)
    pygame.display.flip()
    clock.tick (60)

pygame.quit()
exit()
