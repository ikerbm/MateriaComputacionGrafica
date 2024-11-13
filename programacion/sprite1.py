import pygame
import math
ancho=800
alto=600

if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    pelota=pygame.image.load('New Piskel.png')
    orochi=pygame.image.load('orochi.png')
    print pelota.get_rect()
    print orochi.get_rect()
    posx=100
    posy=200
    velx=0
    vely=0
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    velx=5
                if event.key==pygame.K_LEFT:
                    velx= -5
                if event.key==pygame.K_DOWN:
                    vely=5
                if event.key==pygame.K_UP:
                    vely=-5
                if event.key==pygame.K_SPACE:
                    velx=0
                    vely=0
        if posx> (ancho-32):
            posx=0
        if posx<0:
            posx=ancho-32
        ventana.fill([0,0,0])
        ventana.blit(pelota,[posx,200])
        ventana.blit(orochi,[posx+200,200])
        pygame.display.flip()
        posx+=velx
        posy+=vely
        reloj.tick(60)
