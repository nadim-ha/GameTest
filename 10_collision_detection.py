import pygame , random

#initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Collision detection")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#set game values
VELOCITY = 5

#load images
ezio_image = pygame.image.load("ezio.png")
ezio_rect = ezio_image.get_rect()
ezio_rect.centerx = WINDOW_WIDTH//2
ezio_rect.top = 0

artifact_image = pygame.image.load("artifact.png")
artifact_rect = artifact_image.get_rect()
artifact_rect.centerx = WINDOW_WIDTH//2
artifact_rect.bottom = WINDOW_HEIGHT

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #get a list of all keys pressed
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ezio_rect.left > 0:
        ezio_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and ezio_rect.right < WINDOW_WIDTH:
        ezio_rect.x += VELOCITY
    if keys[pygame.K_UP] and ezio_rect.top > 0:
        ezio_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and ezio_rect.bottom < WINDOW_HEIGHT:
        ezio_rect.y += VELOCITY

    #check for collision
    if ezio_rect.colliderect(artifact_rect):
        print("Indiamo !")
        artifact_rect.left = random.randint(0, WINDOW_WIDTH - 42 ) #deduct 42 (the image pixels) so it doesn't go off the screen
        artifact_rect.top = random.randint(0, WINDOW_HEIGHT - 42)

    #fill display
    display_surface.fill((0, 0, 0))

    #draw recatngles around objects
    pygame.draw.rect(display_surface, (142,229,238), ezio_rect, 1)
    pygame.draw.rect(display_surface, (255,185,15), artifact_rect, 1)

    #blit images
    display_surface.blit(ezio_image, ezio_rect)
    display_surface.blit(artifact_image, artifact_rect)

    #update display
    pygame.display.flip()

    #tick the clock
    clock.tick(FPS)

#end the game
pygame.quit()