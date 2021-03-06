from pygame.locals import *
import pygame
import sys
import time
import random
import math
 
image_resources = "app_resources/image_resources/"
sound_resources = "app_resources/sound_resources/"
 
width,height = 1280,600
size = (width,height)
 
clock = pygame.time.Clock()
FPS = 3000
 
coin_offset = 60
coin2_offset = 60
points = 1
kill_switch = 0
 
def quit_game():
    pygame.quit()
    sys.exit("System exit.")

class load:
    def image(self,image):
        return (image_resources + image)
    def sound(self,sound):
        return (sound_resources + sound)

#image_1 = load().image("bg_solid_black_square.jpg")
#image_2 = load().image("ball_blue.png")





class GetSource:
    def background(self,image):
        return pygame.image.load(image_resources + image).convert()
    def player(self,image):
        return pygame.image.load(image_resources + image).convert_alpha()
   
class Wall(pygame.sprite.Sprite):
    def __init__(self,color,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(pygame.color.Color(color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_resources + image).convert_alpha()
        self.rect = self.image.get_rect()
       
class Coin(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_resources + image).convert_alpha()
        self.rect = self.image.get_rect()

class Coin2(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_resources + image).convert_alpha()
        self.rect = self.image.get_rect()
       
pygame.init()
 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("لعبة ديال لقرد")
background = GetSource().background("test.jpg")
player = GetSource().player("awesome.png").convert_alpha()
player_dimension = player.get_width()
 
x,y = width/2-player_dimension,height/2-player_dimension
movex,movey = 0,0
 
walls = pygame.sprite.Group()
players = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
 
wall_1 = Wall("white", 0, 0, width, 5)
wall_2 = Wall("white", 0, 0, 5, height)
wall_3 = Wall("white", 0, height-5, width, 5)
wall_4 = Wall("white", width-5, 0, 5, height)
player = Player("awesome.png")
coin = Coin("banana.png")
coin2 = Coin2("poop.png")
 
walls.add(wall_1,wall_2,wall_3,wall_4)
players.add(player)
coins.add(coin)
coins.add(coin2)
all_sprites.add(wall_1,wall_2,wall_3,wall_4,player,coin,coin2)


while True:
 
    clock.tick(FPS)
 
    ticks = pygame.time.get_ticks()
   
    collide_list_1 = pygame.sprite.spritecollideany(wall_1,players)
    collide_list_2 = pygame.sprite.spritecollideany(wall_2,players)
    collide_list_3 = pygame.sprite.spritecollideany(wall_3,players)
    collide_list_4 = pygame.sprite.spritecollideany(wall_4,players)
    collide_list_5 = pygame.sprite.spritecollideany(coin, players)
    collide_list_6 = pygame.sprite.spritecollideany(coin2, players)
   
    for event in pygame.event.get():
        if event.type == QUIT:
            quit_game()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit_game()
            elif event.key == K_LEFT or event.key == K_a:
                movex = -4
            elif event.key == K_RIGHT or event.key == K_d:
                movex = 4
            elif event.key == K_UP or event.key == K_w:
                movey = -4
            elif event.key == K_DOWN or event.key == K_s:
                movey = 4
               
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a or event.key == K_RIGHT or event.key == K_d:
                movex = 0
            if event.key == K_UP or event.key == K_w or event.key == K_DOWN or event.key == K_s:
                movey = 0
 
    if collide_list_1 != None:
        movey = 0
        y += 1
    if collide_list_2 != None:
        movex = 0
        x += 1
    if collide_list_3 != None:
        movey = 0
        y -= 1
    if collide_list_4 != None:
        movex = 0
        x -= 1
    else:    
        x += movex
        y += movey
 
    player.rect.x = x
    player.rect.y = y
 
    screen.blit(background, (0,0))
 
    if  kill_switch == 0:
        coin.rect.x = random.randint(0,width-coin_offset)
        coin.rect.y = random.randint(0,height-coin_offset)
        kill_switch = 1

    if  kill_switch == 0:
        coin2.rect.x = random.randint(0,width-coin2_offset)
        coin2.rect.y = random.randint(0,height-coin2_offset)
        kill_switch = 1
       
    #pygame.display.set_caption("Points: "+str(points))
   
    if collide_list_5 != None:
        points += 1
        coin.rect.x = random.randint(0,width-coin_offset)
        coin.rect.y = random.randint(0,height-coin_offset)
        coin2.rect.x = random.randint(0,width-coin2_offset)
        coin2.rect.y = random.randint(0,height-coin2_offset)

    if collide_list_6 != None:
        points -= 2
        coin2.rect.x = random.randint(0,width-coin2_offset)
        coin2.rect.y = random.randint(0,height-coin2_offset)
        coin.rect.x = random.randint(0,width-coin_offset)
        coin.rect.y = random.randint(0,height-coin_offset)


    black = (0, 0, 0) 
    message = "Points: "+str(points)
    font = pygame.font.Font(None, 40)
    text = font.render(message, points, black)
    screen.blit(text, (10,10))                                 

    all_sprites.draw(screen)
    all_sprites.update()
   
    pygame.display.update()

