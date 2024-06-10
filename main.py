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
#temp_rect = temp.get_rect(center=(WIDTH,HEIGHT//5.5))
temp_rect = temp.get_rect()
temp = pygame.transform.scale(temp,(90,HEIGHT/5.5))
#turn into list
temp_rect.x = 380
temp_rect.y = 220
temp_rect_speed=10




score=0
Health = 3

enemy=pygame.image.load("Temp_Enemy.png")
#enemy_rect = enemy.get_rect(center=(WIDTH-20,HEIGHT//1.3))
enemy_rect= enemy.get_rect()
enemy= pygame.transform.scale(enemy,(120,HEIGHT/4.5))

enemy_rect.x=-120
enemy_rect.y=200
enemy_rect_speed: 3

bat=pygame.image.load("bat_enemy.png")
bat_rect= enemy.get_rect()
bat_rect.x = 10
bat_rect.y = 10

fireball=pygame.image.load("temp_fireball.png")
fireball_rect = fireball.get_rect(center=(10,HEIGHT//1.6))
fireball = pygame.transform.scale(fireball,(150,HEIGHT/3))
fireball_rect_speed= 13
fireball_rect.y = temp_rect.y + 151

# Initialize more variables and states below
#

#### TESTING
# if fireball_rect.colliderect(enemy_rect):
#     # do something
###


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
    screen.blit(fireball,fireball_rect)
    screen.blit(bat,bat_rect)

    input=pygame.key.get_pressed()

  #  if enemy_rect.colliderect(temp_rect):

    if  enemy_rect < temp_rect:
        enemy_rect.x +=  6
    elif enemy_rect > temp_rect:
        enemy_rect.x -= 6
        if enemy_rect.colliderect(temp_rect):
            Health -1 
            enemy_rect.x -10

    
   
    if enemy_rect.colliderect(fireball_rect):
        enemy_rect.x = -120
        fireball_rect.x = 600

    if enemy_rect.colliderect(temp_rect):
        Health - 1
        
        

     
    


        


    #if enemy_rect <= temp_rect:
      #  enemy_rect.x += 4
    #elif enemy_rect >= temp_rect:
      #  enemy_rect.x -= 4

    if input[pygame.K_LEFT]:
        temp_rect.x -= temp_rect_speed
    if input[pygame.K_RIGHT]:
        temp_rect.x += temp_rect_speed

    
  
    if input[pygame.K_1]:
     
      fireball_rect.y = temp_rect.y -2
      fireball_rect.x = temp_rect.x - 60
     
    if fireball_rect.x < temp_rect.x:
        fireball_rect.x -= fireball_rect_speed

    
    if input[pygame.K_2]:
      
      fireball_rect.y = temp_rect.y +2
      fireball_rect.x = temp_rect.x + 20
    if fireball_rect.x > temp_rect.x:
        fireball_rect.x += fireball_rect_speed


   # if fireball_rect.colliderect(enemy_rect):
        
       # fireball_rect.x = temp_rect.x -60
       # fireball_rect.x < temp_rect.x
       # fireball_rect.x -= 1
    #elif fireball_rect.x < 400:
        #fireball_rect.x -= 1
       # fireball_rect.x = 1

    #elif fireball_rect < temp_rect:
      #  fireball_rect.x -= 6

       # while fireball_rect not 
      
        
        #while fireball_rect.x >= -150:
       #  fireball_rect.x -= 2

       
 

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 fps

# Quit Pygame   
pygame.quit()
sys.exit()
