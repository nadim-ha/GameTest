import pygame

#initiate pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#define colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Give a background color
display_surface.fill(BLACK)

#test creating lines
pygame.draw.line(display_surface, BLUE, (0,0), (display_surface.get_width() // 2, display_surface.get_height() // 2), 15)
pygame.draw.line(display_surface, BLUE, (display_surface.get_width() // 2, display_surface.get_height() // 2), (0, display_surface.get_height()), 15)
pygame.draw.line(display_surface, BLUE, (display_surface.get_width() // 2, display_surface.get_height() // 2), (display_surface.get_width(), display_surface.get_height()), 15)
pygame.draw.line(display_surface, BLUE, (display_surface.get_width() // 2, display_surface.get_height() // 2), (display_surface.get_width(), 0), 15)

#test creating circles
pygame.draw.circle(display_surface, WHITE, ((display_surface.get_width() // 2) , (display_surface.get_height() // 2) //2), 40, 0)
pygame.draw.circle(display_surface, WHITE, ((display_surface.get_width() // 2) , (display_surface.get_height()-(display_surface.get_height() // 2) //2)), 40, 0)

#test creating rectangles (surface, color,(top-left x, top-left y, width, height))
#pygame.draw.rect(display_surface,WHITE,((display_surface.get_height() // 2),(display_surface.get_width()-(display_surface.get_width() // 2) //2),0,0))
pygame.draw.rect(display_surface,WHITE,((display_surface.get_width() // 8),(display_surface.get_height() // 3.1), 50, 50))


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
