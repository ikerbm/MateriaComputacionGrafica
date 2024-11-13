import pygame
import math
from libreria import*
def linea(coor,origen,v,color):
    pygame.draw.line(v,color,origen,coor)
def corazon(g):
    rad=math.radians(g)
    t1=math.sin(rad)
    t2=math.sqrt(abs(math.cos(rad)))

    t3=(7/5)+math.sin(rad)
    t3+=0.00000001
    print(t3)
    t4=2*math.sin(rad)
    r=t1*(t2/t3)-t4
    print(r)
    r=math.sin(rad)*((math.sqrt(abs(math.cos(rad))))/(math.sin(rad)+7/5))-2*math.sin(rad)
    return r
if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    plano(ventana)

    g=1
    i=1
    while(i<=359):

        c=corazon(g)
        cp=polar_pan(c,g)
        ct=pan_car(cp,origen)
        linea(ct,origen,ventana,rojo)

        g=g+1
        i=i+1


    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            pygame.display.flip()
