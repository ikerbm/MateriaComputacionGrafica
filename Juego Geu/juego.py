import pygame
import random
import math

ANCHO=1200
ALTO=800
NEGRO=[0,0,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Gato(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.vida=3

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Generador(pygame.sprite.Sprite):
    def __init__(self,pos,dim):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=random.randrange(20)

    def update(self):
        self.temp-=1

class Raton(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.dir=0
        self.image=pygame.Surface([10,10])
        self.image.fill(NEGRO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Linea(pygame.sprite.Sprite):
    def __init__(self,pos,dimb):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dimb)
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.dir=0
        self.velx=0
        self.vely=0
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, dimensiones=[100,100]):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dimensiones)
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

if __name__ == '__main__':
    pygame.init()
    #Definicion pantalla
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    fin=False
    reloj=pygame.time.Clock()
    #Definicion de imagenes
    fondo=pygame.image.load('mont.jpg')
    info=fondo.get_rect()
    f_ancho=info[2]
    f_alto=info[3]
    fx=0
    fy=0
    fvelx= 0
    fvely = 0
    lim_der=1000
    lim_iz=200
    lim_ar=100
    lim_ab=700
    #creacion grupos
    gatos=pygame.sprite.Group()
    ratones=pygame.sprite.Group()
    generadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    #creacion del gato
    g=Gato([ALTO/2,ANCHO/2])
    gatos.add(g)

    #creacion generadores de enemigos
    b=Generador([300,350],[50,60])
    generadores.add(b)

    #creacion lineas imaginarias
    lineas=pygame.sprite.Group()
    l=Linea([0,0],[5,ALTO*3])
    l.dir=3
    lineas.add(l)
    l2=Linea([0,0],[ANCHO*3,5])
    l2.dir=2
    lineas.add(l2)
    l3=Linea([(ANCHO*3)-5,0],[5,ALTO*3])
    l3.dir=0
    lineas.add(l3)
    l4=Linea([0,(ALTO*3)-5],[ANCHO*3,5])
    l4.dir=1
    lineas.add(l4)

    #creacion de bloques
    b=Bloque([1100,700])
    bloques.add(b)

    b1=Bloque([1900,50])
    bloques.add(b1)
    while(not fin):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    g.velx=5
                    g.vely=0
                if event.key == pygame.K_LEFT:
                    g.velx= -5
                    g.vely=0
                if event.key == pygame.K_UP:
                    g.velx=0
                    g.vely=-5
                if event.key == pygame.K_DOWN:
                    g.velx= 0
                    g.vely= 5
            if event.type == pygame.KEYUP:
                g.velx=0
                g.vely=0
                fvelx=0
                fvely=0
                for b in bloques:
                    b.velx=0
                    b.vely=0
                for l in lineas:
                    l.velx=0
                    l.vely=0

        #desplazamiento de la pantalla y los objetos
        #cuando el jugador se mueve mas alla del fondo
        if g.rect.right > lim_der:
            g.rect.right = lim_der
            g.velx=0
            fvelx=-5
            for b in bloques:
                b.velx=-5
            for l in lineas:
                l.velx=-5
            for r in ratones:
                r.velx=-5

        if g.rect.right < lim_iz:
            g.rect.right = lim_iz
            g.velx=0
            fvelx=5
            for b in bloques:
                b.velx=5
            for l in lineas:
                l.velx=5
            for r in ratones:
                r.velx=5

        if g.rect.top > lim_ab:
            g.rect.top = lim_ab
            g.vely=0
            fvely=-5
            for b in bloques:
                b.vely=-5
            for l in lineas:
                l.vely=-5
            for r in ratones:
                r.vely=-5

        if g.rect.bottom < lim_ar:
            g.rect.bottom = lim_ar
            g.vely=0
            fvely=5
            for b in bloques:
                b.vely=5
            for l in lineas:
                l.vely=5
            for r in ratones:
                r.vely=5

        if fx < (ANCHO-f_ancho):
            fx+=5
            fvelx=0
            for b in bloques:
                b.velx=0
        if fx > (f_ancho):
            fx-=5
            fvelx=0
            for b in bloques:
                b.velx=0

        for g1 in generadores:
            if g1.temp<0:
                g1.temp=random.randrange(20)
                r=Raton(g1.rect.center)
                if g1.temp<5:
                    r.velx=5
                    r.dir=2
                elif g1.temp<10:
                    r.velx=-5
                    r.dir=1
                elif g1.temp<15:
                    r.vely=-5
                    r.dir=3
                elif g1.temp<20:
                    r.vely=5
                    r.dir=0
                ratones.add(r)

        for g in gatos:
            ls_k=pygame.sprite.spritecollide(g,ratones,True)
        for r in ratones:
            ls_l=pygame.sprite.spritecollide(r,lineas,False)
            for l in ls_l:
                if l.dir==2:
                    r.velx=5
                    r.vely=0
                if l.dir==1:
                    r.velx=-5
                    r.vely=0
                if l.dir==0:
                    r.velx=0
                    r.vely=5
                if l.dir==3:
                    r.velx=0
                    r.vely=-5
                r.dir=l.dir

        #actualizaciones
        gatos.update()
        generadores.update()
        bloques.update()
        ratones.update()
        lineas.update()
        ventana.blit(fondo, [fx,fy])
        ratones.draw(ventana)
        generadores.draw(ventana)
        gatos.draw(ventana)
        lineas.draw(ventana)
        bloques.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
        fx+=fvelx
        fy+=fvely
