from os import access
import pygame

#initiate pygame
pygame.init()

#create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

#left image conf
AC_left_logo = pygame.image.load("assassins-creed.png")
AC_left_logo_rect = AC_left_logo.get_rect()
AC_left_logo_rect.topleft = (0,0)

#right image conf
AC_right_logo = pygame.image.load("assassins-creed.png")
AC_right_logo_rect = AC_right_logo.get_rect()
AC_right_logo_rect.topright = ((display_surface.get_width()),0)

#update blit
display_surface.blit(AC_left_logo,AC_left_logo_rect)
display_surface.blit(AC_right_logo,AC_right_logo_rect)

pygame.draw.line(display_surface,(255,255,255),(0,110),(WINDOW_WIDTH,110),5)
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
