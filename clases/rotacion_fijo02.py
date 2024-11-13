import pygame
from lib.grafica import *


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    ls=[[50,100],[100,100],[100,150]]

    reloj=pygame.time.Clock()
    a=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        #Paso 1 definir punto fijo
        P=[100,100]
        T=[-100,-100]

        #Paso 2 Trasladar puntos usando T
        ls_t=[]
        for p in ls:
            pt=Trasladar(p,T)
            ls_t.append(pt)

        print ls_t

        #3. Rotar puntos trasladados

        ls_r=[]
        for p in ls_t:
            pr=Rotacion(p,a)
            ls_r.append(pr)

        print ls_r

        #4. Trasladar al lugar original con T=P
        T=P
        ls_f=[]
        for p in ls_r:
            pf=Trasladar(p,T)
            ls_f.append(pf)

        print ls_f

        

        pantalla.fill(NEGRO)
        pygame.draw.polygon(pantalla,BLANCO,ls,1)
        #pygame.draw.polygon(pantalla,BLANCO,ls_t,1)
        #pygame.draw.polygon(pantalla,VERDE,ls_r,1)
        pygame.draw.polygon(pantalla,VERDE,ls_f,1)
        pygame.display.flip()

        reloj.tick(40)
        a+=10