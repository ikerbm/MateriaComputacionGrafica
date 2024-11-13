import pygame
import random

ANCHO=800
ALTO=600
NEGRO=[0,0,0]
BLANCO=[255,255,255]
ROJO=[255,0,0]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos,tamano):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(tamano)
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.plataformas=None


    def gravedad(self,g=0.5):
        if self.vely==0:
            self.vely=0.5
        else:
            self.vely+=0.5


    def update(self):
        self.rect.x+=self.velx
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
            if self.velx > 0:
                if self.rect.right>b.rect.left:
                    self.rect.right=b.rect.left
                    self.velx=0
            else:
                if self.rect.left<b.rect.right:
                    self.rect.left=b.rect.right
                    self.velx=0
        self.rect.y+=self.vely
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
            if self.vely > 0:
                if self.rect.bottom>b.rect.top:
                    self.rect.bottom=b.rect.top
                    self.vely=0
            else:
                if self.rect.top<b.rect.bottom:
                    self.rect.top=b.rect.bottom
                    self.vely=0
        self.gravedad()
        if self.rect.bottom >ALTO:
            self.rect.bottom=ALTO
            self.vely=0


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, pos,tamano):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(tamano)
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0


if __name__ =='__main__':
    pygame.init()
    #definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    jugadores=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    j=Jugador([100,100],[50,70])
    p=Plataforma([400,400],[100,50])
    p1=Plataforma([500,300],[100,50])
    jugadores.add(j)
    plataformas.add(p)
    plataformas.add(p1)
    j.plataformas=plataformas

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    j.velx=5
                if event.key==pygame.K_a:
                    j.velx=-5
                if event.key==pygame.K_SPACE:
                    j.vely=-10
            if event.type==pygame.KEYUP:
                j.velx=0


        jugadores.update()
        plataformas.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        plataformas.draw(ventana)
        reloj.tick(20)
        pygame.display.flip()
