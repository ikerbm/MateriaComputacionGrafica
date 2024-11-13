import pygame
import math
from libreria import*
def linea(coor,origen,v,color):
    pygame.draw.line(v,color,origen,coor)
def florcos(a,b,g):
    rad=math.radians(g)
    r=a*math.sin(b*rad)
    return r
if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    plano(ventana)
    a=200
    b=10
    g=0
    i=0
    while(i<=360):
        r=flor(a,b,g)
        rp=polar_pan(r,g)
        rt=pan_car(rp,origen)
        c=florcos(a,b,g)
        cp=polar_pan(c,g)
        ct=pan_car(cp,origen)
        linea(ct,origen,ventana,morado)
        linea(rt,origen,ventana,azul)
        g=g+1
        i=i+1


    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            pygame.display.flip()
