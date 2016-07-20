import pygame
pygame.init()

def screen ():
    #screen size
    size = [800, 520]   
    pygame.display.set_mode(size)
    #text dyal la barre dyal lwindow
    pygame.display.set_caption('لعبة ديال القرد ')
    #loop bach tsed lwindow
    done = False
    while not done:
       for event in pygame.event.get(): # if the user does chi 7aja
            if event.type == pygame.QUIT: # If user clicked close
                done=True # loop is done




pygame.quit()






