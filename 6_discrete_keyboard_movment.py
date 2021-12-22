import pygame

#initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement")

#set game values
VELOCITY = 10

#load in images
ezio_image = pygame.image.load("Ezio.png")
ezio_rect = ezio_image.get_rect()
ezio_rect.centerx = WINDOW_WIDTH//2
ezio_rect.top = 0



#The main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


        #check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ezio_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                ezio_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                ezio_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                ezio_rect.y += VELOCITY

    #Fi9ll the display
    display_surface.fill((0, 0, 0))

    #blit image to display 
    display_surface.blit(ezio_image, ezio_rect)

    #update the display
    pygame.display.flip()

#end the game
pygame.quit()