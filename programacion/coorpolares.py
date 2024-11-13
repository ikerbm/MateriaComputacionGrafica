import pygame
import math
from libreria import*



def linea(coor,origen,v):
    pygame.draw.line(v,rojo,origen,coor)


if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([alto,ancho])
    plano(ventana)
    a=30
    b=50
    g=0
    i=0
    while(i<=360):
        r=cardioide(a,b,g)
        rp=polar_pan(r,g)
        rt=pan_car(rp,origen)

        linea(rt,origen,ventana)
        g=g+1
        i=i+1


    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True





        pygame.display.flip()
