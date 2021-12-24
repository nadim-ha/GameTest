import pygame

#initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement")

#set game values
VELOCITY = 10

#load images
ezio_image = pygame.image.load("ezio.png")
ezio_rect = ezio_image.get_rect()

ezio_rect.centerx = WINDOW_WIDTH//2
ezio_rect.top = 0

#the main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.mouse.get_pressed():
    
    #fill display
    display_surface.fill((0, 0, 0))

    #blit assets
    display_surface.blit(ezio_image, ezio_rect)

    #update the display
    pygame.display.flip()


#end the game
pygame.quit()