"""
Author: YOUR NAME
Date: YYYY-MM-DD
Description: Description of your program here.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Last Stand")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#get background
background = pygame.image.load("First_Spawn.png")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

temp = pygame.image.load("PlaceHolder.png")
temp_rect = temp.get_rect(center=(WIDTH-120,HEIGHT//5.5))
temp = pygame.transform.scale(temp,(270,HEIGHT/2))
#turn into list
temp_rect.x = 380
temp_rect.y = 170
temp_rect_speed=16

enemy=pygame.image.load("Temp_Enemy.png")
enemy_rect = enemy.get_rect(center=(WIDTH-20,HEIGHT//1.3))
enemy= pygame.transform.scale(enemy,(300,HEIGHT/2))

enemy_rect.x=-120
enemy_rect.y=170

fireball=pygame.image.load("temp_fireball.png")
fireball_rect = fireball.get_rect(center=(10,HEIGHT//1.6))
fireball = pygame.transform.scale(fireball,(150,HEIGHT/3))
fireball_rect_speed= 6
fireball_rect.y = temp_rect.y + 151

# Initialize more variables and states below
#

# Define main loop
running = True
clock = pygame.time.Clock()  # Initialize clock object to cap frame rate

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state

    # Draw graphics and output
    #screen.fill(WHITE)

    screen.blit(background,(1,0))
    screen.blit(temp,temp_rect)
    screen.blit(enemy,enemy_rect)

    input=pygame.key.get_pressed()



    if input[pygame.K_LEFT]:
        temp_rect.x -= temp_rect_speed

    if input[pygame.K_RIGHT]:
        temp_rect.x += temp_rect_speed

    if input[pygame.K_1]:
        screen.blit(fireball,fireball_rect)
        fireball_rect.x = temp_rect.x + 10
        fireball_rect.x -= 10
      
        
       # while fireball_rect.x >= -150:
        # fireball_rect.x -= 2
        print (temp_rect)
       
        

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 fps

# Quit Pygame   
pygame.quit()
sys.exit()
