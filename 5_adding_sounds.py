import pygame

#initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

#load background music
pygame.mixer.music.load('forest.wav')
#Load sound effects
sound1 = pygame.mixer.Sound('sound1.wav')
sound2 = pygame.mixer.Sound('sound2.wav')

#play and stop the music
pygame.mixer.music.play(-1, 0.0)
#Play the sound effects
sound1.play()
pygame.time.delay(1000)
sound2.play()
#pygame.time.delay(2000)
pygame.time.delay(5000)
pygame.mixer.music.stop()


#change volume
sound2.set_volume(.5)
sound2.play()

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#end the game
pygame.quit()