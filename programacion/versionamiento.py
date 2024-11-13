import pygame
import random
from libreria import*
class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(blanco)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
class Rival(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(rojo)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0


if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    reloj=pygame.time.Clock()
    fin=False
    jugadores=pygame.sprite.Group()
    rivales=pygame.sprite.Group()

    j=Jugador([100,200])
    jugadores.add(j)

    n=10
    for i in range(n):
        x=random.randrange(ancho)
        y=random.randrange(alto)
        r=Rival([x,y])
        rivales.add(r)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key==pygame.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key==pygame.K_UP:
                    j.vely=-5
                    j.velx=0
                if event.key==pygame.K_DOWN:
                    j.vely=5
                    j.velx=0
            if event.type==pygame.KEYUP:
                j.vely=0
                j.velx=0

        #control
        #refresco
        jugadores.update()
        ventana.fill(negro)
        jugadores.draw(ventana)
        rivales.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
