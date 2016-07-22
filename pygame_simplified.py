import pygame
from pygame.locals import*
import random
#define some colors
black= (0,0,0)
white= (255,255,255)
red=(255,0,0)
green= (0,255,0)
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
#bouncing ball class code
class BouncingBall():
    #constructor method
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):
     #attributes of the bouncing ball
        self.x_location=x_location
        self.y_location=y_location
        self.x_speed=x_speed
        self.y_speed=y_speed
        self.ball_size=ball_size
    
    #ball methods
    #flash and bounce: the actions the ball can perform
    def flashBounce(self, screen, colors, screen_width, screen_height):
        ball_color=random.choice(colors) #is outside because of variable scoping
        if self.x_location>=screen_width-self.ball_size or self.x_location < self.ball_size:
            self.x_speed=self.x_speed*-1
        if self.y_location>=screen_height-self.ball_size or self.y_location < self.ball_size:
            self.y_speed=self.y_speed*-1

        self.x_location+=self.x_speed
        self.y_location+=self.y_speed

        pygame.draw.circle(screen,ball_color, [self.x_location, self.y_location],
        self.ball_size)

Ping_pong =BouncingBall(250,350,10,10,4)
    
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(green)
    Ping_pong.flashBounce(screen,possible_ball_colors, screen_width,screen_height)
    pygame.display.flip()
    clock.tick (60)

pygame.quit()
exit()

            
    
