import pygame

#initiate pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption(" Blitting Text ")


#Define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

#check available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

#define fonts
system_font = pygame.font.SysFont('calibri', 32)
custom_font = pygame.font.Font('BlackgroundsRegular.ttf', 65)

#define text:
system_text = system_font.render('Coming this winter', True, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100)

custom_text = custom_font.render('ATTACK ON TITAN', True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#blit the text surface
display_surface.blit(system_text, system_text_rect)
display_surface.blit(custom_text, custom_text_rect)

#update display
pygame.display.flip()

#main game loop
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
    
#End the game
pygame.quit()      

test nadim