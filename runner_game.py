


import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
TURQUOISE=(40,200,120)
PURPLE= (100,40,200)
YELLOW= (160,160,0)
PINK=(230,50,230)

colors = [BLACK, GREEN, BLUE, RED,TURQUOISE, PURPLE, YELLOW, PINK]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("Runner_game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#import city scroller
from city_scroller_me2 import Scroller

class RunnerSprite (pygame.sprite.Sprite):
    def __init__(self,size,color,image):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.color=color
        #self.image=pygame.Surface((20,20))
        self.image = pygame.image.load(image)
        


        #self.image.fill(PINK)
        self.rect=self.image.get_rect()
                
        
Jojo = RunnerSprite(4, TURQUOISE, "penny_proud.jpg")
    


    

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT-50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT-100), BACK_SCROLLER_COLOR, 1)



all_sprites = pygame.sprite.Group()
all_sprites.add(Jojo)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # --- Game logic should go here
        #pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEMOTION:
            (mouseX,mouseY)= pygame.mouse.get_pos()
            Jojo.rect.x=mouseX
            Jojo.rect.y=mouseY
       

    #http://stackoverflow.com/questions/26451227/how-to-make-an-image-follow-the-mouse-cursor-in-pygame
    



    #pygame.Rect.move_ip(mouse_position)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    back_scroller.add_buildings()
    back_scroller.draw_buildings(screen)
    back_scroller.move_buildings()
    middle_scroller.add_buildings()
    middle_scroller.draw_buildings(screen)
    middle_scroller.move_buildings()
    front_scroller.add_buildings()
    front_scroller.draw_buildings(screen)
    front_scroller.move_buildings()
    all_sprites.draw(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
