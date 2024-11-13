import pygame
import random

ANCHO=1200
ALTO=800

VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
AMARILLO=[200,200,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=350
        self.velx=0
        self.vely=0
        self.salud=300

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, dimensiones=[100,100]):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dimensiones)
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0

    def update(self):
        self.rect.x+=self.velx

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fondo=pygame.image.load('mont.jpg')
    info=fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    print 'ancho fondo: ', f_ancho, ' alto fondo: ', f_alto
    fx=0
    fvelx= 0
    fy=0
    fvely = 0
    lim_der=1000
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    j=Jugador()
    jugadores.add(j)

    b=Bloque([1100,700])
    bloques.add(b)

    b1=Bloque([1900,50])
    bloques.add(b1)

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.velx= -5
                    j.vely=0
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-5
                if event.key == pygame.K_DOWN:
                    j.velx= 0
                    j.vely= 5
            if event.type == pygame.KEYUP:
                j.velx=0
                j.vely=0
                fvelx=0
                for b in bloques:
                    b.velx=0

        if j.rect.right > lim_der:
            j.rect.right = lim_der
            j.velx=0
            fvelx=-5
            for b in bloques:
                b.velx=-5

        if fx < (ANCHO-f_ancho):
            fx+=5
            fvelx=0
            for b in bloques:
                b.velx=0

        jugadores.update()
        bloques.update()
        pantalla.blit(fondo, [fx,fy])
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
        fx+=fvelx
        print fx
        #fy+=fvely
