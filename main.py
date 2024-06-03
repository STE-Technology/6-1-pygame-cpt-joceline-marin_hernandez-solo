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
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Last Stand")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#get background
background = pygame.image.load("First_Spawn.png")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

temp = pygame.image.load("PlaceHolder.png")
temp_rect = temp.get_rect(center=(WIDTH-10,HEIGHT//1.5))
temp = pygame.transform.scale(temp,(270,HEIGHT/2))
#turn into list
temp_rect.x = 380
temp_rect.y = 260
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
    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 fps

# Quit Pygame   
pygame.quit()
sys.exit()
