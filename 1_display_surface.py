import pygame

#initiate pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Hello World :) ")

#main game loop
running = True
while running:
   for event in pygame.event.get():
       print(event)
       if event.type == pygame.QUIT:
           running = False

#End the game
pygame.quit()      
