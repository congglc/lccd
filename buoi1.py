import pygame , sys
from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((1280,768))
pygame.display.set_caption("my game")
#fps
clock= pygame.time.Clock()
#player
player1=pygame.image.load('player/idle.png').convert()
player1=pygame.transform.scale2x(player1)
player1_rect = player1.get_rect(center =(100,100) )
class Player:
    def __init__(self, x , y, width , height):
        self.x =x
        self.y = y
        self.width =width
        self.height = height
    def main(self,DISPLAY):
        pygame.draw.rect(DISPLAY, (255,0,0),(self.x, self.y, self.width, self.height))
        
DISPLAY_croll   = [0,0]  
#bacground
bgr=pygame.image.load('background/bg.jpg').convert()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys= pygame.key.get_pressed()            
    if keys[pygame.K_UP]:
        DISPLAY_croll[0]-=5
    if keys[pygame.K_DOWN]:
        DISPLAY_croll[0]+=5
    if keys[pygame.K_LEFT]:
        DISPLAY_croll[1]-=5
    if keys[pygame.K_RIGHT]:
        DISPLAY_croll[1]+=5 
        
            
             
    pygame.display.update()
    DISPLAY.blit(bgr,(0,0))
    DISPLAY.blit(player1,player1_rect)
    clock.tick(120)
            
            
        
   









