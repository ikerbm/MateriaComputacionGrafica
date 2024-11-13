import pygame
import random
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

ANCHO=800
ALTO=600
NEGRO=[0,0,0]
ROJO=[255,0,0]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos,sabana):
        pygame.sprite.Sprite.__init__(self)
        self.sabana=sabana
        self.accion=8
        self.con=0
        self.image=self.sabana[self.accion][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.movimiento=False
        self.vida=3
        self.puntos=0
    def update(self):
        if self.movimiento:
            if self.con < 6:
                self.con+=1
            else:
                self.con=1
            self.image=self.sabana[self.accion][self.con]
            self.rect.x+=self.velx
        else:
            self.image=self.sabana[self.accion][0]

    def RetPos(self):
        if self.accion==11:
            x=self.rect.x+32
            y=self.rect.y
            return[x,y]
        if self.accion==10:
            x=self.rect.x
            y=self.rect.y
            return[x,y]



class Bala(pygame.sprite.Sprite):
    def __init__(self,pos,sabanae):
        pygame.sprite.Sprite.__init__(self)
        self.dir=0
        self.con=0
        self.sabanae=sabanae
        self.image=self.sabanae[self.dir][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0
        self.velx=0
        self.f_velx=0
        self.f_vely=0
    def update(self):
        if self.con<7:
            self.con+=1
        else:
            self.con=0
        self.image=self.sabanae[self.dir][self.con]
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely


if __name__ == '__main__':
    pygame.init()
    #Definiciones
    #Definicion pantalla
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    #Definicion imagenes
    rain=pygame.image.load('Rain.png')
    airship=pygame.image.load('Airship.jpg')
    valhalla=pygame.image.load('valhalla.jpg')
    aldore=pygame.image.load('Aldore Tower.jpg')
    balaj=pygame.image.load('fireball.png')
    #recorte de imagenes
    sabanarain=[]
    for j in range(25):
        col=[]
        for i in range(7):
            sprite=rain.subsurface(64*i,64*j,64,64)
            col.append(sprite)
        sabanarain.append(col)

    sabanabalaj=[]
    for j in range(8):
        col=[]
        for i in range(8):
            sprite=balaj.subsurface(64*i,64*j,64,64)
            col.append(sprite)
        sabanabalaj.append(col)

    #Definicion fuentes
    fuente=pygame.font.Font(None,34)
    fuente_prev=pygame.font.Font(None,46)
    fuente_perder=pygame.font.Font(None,60)
    #Definicion musica
    combate=pygame.mixer.Sound('Simons Theme.ogg')
    intro=pygame.mixer.Sound('Zelda Theme.ogg')
    victoria=pygame.mixer.Sound('Fairy tail Theme.ogg')
    game_over=pygame.mixer.Sound('sadness and sorrow.ogg')
    #Definicion mensajes
    mensajep=fuente_perder.render('FIN DEL JUEGO',True,BLANCO)
    mensajev=fuente_perder.render('FELICITACIONES',True,ROJO)
    mensajev2=fuente.render('gracias por jugar',True,ROJO)
    titulo=fuente_prev.render('BIENVENIDO',True,BLANCO)
    instruccion=fuente_prev.render('presione una tecla para continuar',True,BLANCO)

    #seccion antes del inicio del juego
    intro.play()
    fin=False
    fin_prev=False
    ganador=False
    perdedor=False
    while(not fin) and (not fin_prev):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                fin_prev=True
        ventana.blit(valhalla,[0,0])
        ventana.blit(titulo,[300,275])
        ventana.blit(instruccion,[150,325])
        pygame.display.flip()
    intro.stop()
    ventana.fill(NEGRO)
    #Seccion durante el juego
    #Definicion de variables
    f_posx=0
    f_posy=0
    f_velx=0
    f_vely=0
    margen=[[0,40],[ANCHO,40],[ANCHO,0],[0,0]]
    reloj=pygame.time.Clock()
    fin_juego=False
    #Definicion grupos
    jugadores=pygame.sprite.Group()
    barrets=pygame.sprite.Group()
    finas=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    #Reproduccion de musica
    combate.play()
    #Posicionamiento jugador-enemigos
    j=Jugador([64*3,64*4],sabanarain)
    jugadores.add(j)

    while (not fin)and (not fin_juego):
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            #Movimientos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    j.movimiento=True
                    j.accion=11
                    j.velx=10
                    j.vely=0
                if event.key == pygame.K_a:
                    j.movimiento=True
                    j.accion=10
                    j.velx= -10
                    j.vely=0
                if event.key == pygame.K_w:
                    j.movimiento=True
                    j.accion=9
                    j.vely= -10
                    j.velx=0
                if event.key == pygame.K_s:
                    j.movimiento=True
                    j.accion=8
                    j.vely= 10
                    j.velx=0
            if event.type == pygame.KEYUP:
                j.movimiento=False
                j.vely=0
                j.velx=0
                f_velx=0
                f_vely=0
            #Disparo Jugador
            if event.type==pygame.MOUSEBUTTONDOWN:
                #pos jugador
                #disparo_j.play()

                if j.accion==10:
                    p=j.RetPos()
                    b=Bala(p,sabanabalaj)
                    b.velx=-15
                    b.dir=0
                    balas.add(b)
                if j.accion==11:
                    p=j.RetPos()
                    b=Bala(p,sabanabalaj)
                    b.velx=+15
                    b.dir=4
                    balas.add(b)
        #Control
        if j.rect.y > ALTO-j.rect.width:
            j.rect.y=ALTO-j.rect.width
        if j.rect.y < 40:
            j.rect.y=40
        if j.rect.x < 0:
            j.rect.x=0
        if j.rect.x>650:
            j.rect.x=650
            j.velx=0
            f_velx=-10
        if j.rect.x<100:
            j.rect.x=100
            j.velx=0
            f_velx=10
        if j.rect.y>500:
            j.rect.y=500
            j.vely=0
            f_vely=-10
        if j.rect.y<150:
            j.rect.y=150
            j.vely=0
            f_vely=10


        #condiciones fin del JUEGO
        for j in jugadores:
            if j.vida<1:
                perdedor=True
                fin_juego=True
        #Refresco
        ventana.fill(NEGRO)
        Estado_j='VIDAS: '+str(j.vida)
        puntaje='PUNTAJE: '+str(j.puntos)
        info=fuente.render(Estado_j,True,BLANCO)
        puntos=fuente.render(puntaje,True,BLANCO)
        #actualizaciones
        jugadores.update()
        balas.update()

        #dibujado
        jugadores.draw(ventana)
        balas.draw(ventana)
        #acabado
        pygame.draw.polygon(ventana,NEGRO,margen)
        ventana.blit(info,[10,10])
        ventana.blit(puntos,[610,10])
        pygame.display.flip()
        reloj.tick(15)

    #Corte de musica
    combate.stop()
    #Despues del juego

    if perdedor:
        game_over.play()
    else:
        victoria.play()

    while not fin:
        if perdedor:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
            ventana.blit(airship,[0,0])
            ventana.blit(mensajep,[300,286])
            pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    fin=True
                ventana.blit(aldore,[0,0])
                ventana.blit(mensajev,[275,275])
                ventana.blit(mensajev2,[350,325])
                pygame.display.flip()
