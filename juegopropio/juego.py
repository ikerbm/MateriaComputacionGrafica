import pygame
import random
import math

ANCHO=800
ALTO=600
NEGRO=[0,0,0]
ROJO=[255,0,0]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos,pj):
        pygame.sprite.Sprite.__init__(self)
        self.image=pj
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=(ALTO - self.rect.height)-10
        self.velx=0
        self.vely=0
        self.vida=3
        self.puntos=0
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

    def RetPos(self):
        x=self.rect.x+50
        y=self.rect.y+20
        return[x,y]
class Rival(pygame.sprite.Sprite):
    def __init__(self, pos, pj):
        pygame.sprite.Sprite.__init__(self)
        self.image=pj
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.tmp=random.randrange(10,30)
    def RetPos(self):
        x=self.rect.left
        y=self.rect.y +20
        return[x,y]
    def update(self):
        self.tmp -=1
        self.rect.y+=self.vely
        if self.rect.y > (ALTO - self.rect.width):
            self .rect.y= ALTO - self.rect.width
            self.vely = -5
        if self.rect.y < 40:
            self .rect.y= 40
            self.vely = 5
        self.rect.y+=self.vely
class Bala(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,10])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0
        self.velx=0
    def update(self):
        self.rect.x+=self.velx
if __name__ == '__main__':
    pygame.init()
    #Definiciones
    #Definicion pantalla
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    #Definicion imagenes
    lasswell=pygame.image.load('Lasswell sprite.png')
    edward=pygame.image.load('edward.png')
    orochi=pygame.image.load('orochi.png')
    espacio=pygame.image.load('espacio.jpg')
    airship=pygame.image.load('Airship.jpg')
    valhalla=pygame.image.load('valhalla.jpg')
    filas=[]
    for j in range(8):
        col=[]
        for i in range(7):
            sprite=lasswell.subsurface(63*i,63*j,64,64)
            col.append(sprite)
        filas.append(col)
    #Definicion fuentes
    fuente=pygame.font.Font(None,34)
    fuente_prev=pygame.font.Font(None,46)
    fuente_perder=pygame.font.Font(None,60)
    #Definicion musica
    combate=pygame.mixer.Sound('Batalla por la Libertad.ogg')
    game_over=pygame.mixer.Sound('Vals de su jardin.ogg')
    intro=pygame.mixer.Sound('Lyonesse.ogg')
    disparo_j=pygame.mixer.Sound('knifesharpener1.ogg')
    disparo_r=pygame.mixer.Sound('knifesharpener2.ogg')
    #Definicion mensajes
    lasswellmsj=fuente_prev.render('LASSWELL',True,BLANCO)
    mensaje=fuente_perder.render('FIN DEL JUEGO',True,BLANCO)
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

    #Seccion durante el juego
    #Definicion de variables
    reloj=pygame.time.Clock()
    fin_juego=False
    #Definicion grupos
    jugadores=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    #Reproduccion de musica
    combate.play()
    #Posicionamiento jugador-enemigos
    j=Jugador([10,ALTO/2],filas[3][0])
    jugadores.add(j)
    #Numero de enemigos
    n=10
    for i in range(n):
        x=random.randrange(100,ANCHO)
        y=random.randrange(40,ALTO-150)
        vy=random.randrange(1,10)
        r=Rival([x,y],orochi)
        r.vely=vy
        rivales.add(r)

    while (not fin)and (not fin_juego):
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            #Movimientos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_a:
                    j.velx= -5
                    j.vely=0
                if event.key == pygame.K_w:
                    j.vely= -5
                    j.velx=0
                if event.key == pygame.K_s:
                    j.vely= 5
                    j.velx=0
            if event.type == pygame.KEYUP:
                j.vely=0
                j.velx=0
            #Disparo Jugador
            if event.type==pygame.MOUSEBUTTONDOWN:
                #pos jugador
                #disparo_j.play()
                p=j.RetPos()
                b=Bala(p,BLANCO)
                b.velx=+10
                balas.add(b)
        #Control
        if j.rect.y > ALTO-j.rect.width:
            j.rect.y=ALTO-j.rect.width
        if j.rect.y < 40:
            j.rect.y=40
        #Control de rivales
        for r in rivales:
            if r.tmp < 0:
                #disparo_r.play()
                pos=r.RetPos()
                b=Bala(pos,ROJO)
                b.velx=-10
                balas_r.add(b)
                r.tmp=random.randrange(40,90)
        #Limpieza de la memoria
        eliminacion=False
        for b in balas:
            ls_r=pygame.sprite.spritecollide(b,rivales,True)
            if b.rect.y > ANCHO:
                balas.remove(b)
            for r in ls_r:
                j.puntos+=100
                balas.remove(b)
        for b in balas_r:
            ls_j=pygame.sprite.spritecollide(b,jugadores,False)
            if b.rect.x < 0:
                balas_r.remove(b)
            contacto=True
            for j in ls_j:
                if contacto:
                    j.vida-=1
                    balas_r.remove(b)
                    contacto=False

        #condiciones fin del JUEGO
        for j in jugadores:
            if j.vida<1:
                perdedor=True
                fin_juego=True
        #Refresco
        ventana.blit(espacio,[0,0])
        Estado_j='VIDAS: '+str(j.vida)
        puntaje='PUNTAJE: '+str(j.puntos)
        info=fuente.render(Estado_j,True,BLANCO)
        puntos=fuente.render(puntaje,True,BLANCO)
        jugadores.update()
        rivales.update()
        balas.update()
        balas_r.update()
        pygame.draw.line(ventana,BLANCO,[0,40],[ANCHO,40])
        ventana.blit(info,[10,10])
        ventana.blit(puntos,[610,10])
        jugadores.draw(ventana)
        rivales.draw(ventana)
        balas.draw(ventana)
        balas_r.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
    #Corte de musica
    combate.stop()
    #Despues del juego
    if ganador:
        while not fin:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    fin=True
                ventana.fill(NEGRO)
                pygame.display.flip()
    if perdedor:
        game_over.play()
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
            ventana.blit(airship,[0,0])
            ventana.blit(mensaje,[300,286])
            pygame.display.flip()
        game_over.stop()
