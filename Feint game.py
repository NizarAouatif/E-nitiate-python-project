import pygame
from pygame import *
pygame.init()

#screen size
screen = pygame.display.set_mode((800, 600))

#text dyal la barre dyal lwindow
pygame.display.set_caption('لعبة ديال القرد ')



background_image = pygame.image.load("test.jpg").convert()

screen.blit(background_image, (0, 0))
pygame.display.flip()
                                  
#loop bach tsed lwindow
done = False
                                  
while not done:
    for event in pygame.event.get(): # if the user does chi 7aja
            if event.type == pygame.QUIT: # If user clicked close
                done=True # loop is done
                




                
pygame.quit()





