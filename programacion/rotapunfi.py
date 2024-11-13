import pygame
import math
from libreria import*

def triangulo(v,a,b,c):
    pygame.draw.line(ventana,[255,0,0],a,b)
    pygame.draw.line(ventana,[255,0,0],c,b)
    pygame.draw.line(ventana,[255,0,0],a,c)

def trasl(coor,evento):
    if evento == 273:
        coor[1]=coor[1]-10
        return coor
    if evento == 274:
        coor[1]=coor[1]+10
        return coor
    if evento == 276:
        coor[0]=coor[0]-10
        return coor
    if evento == 275:
        coor[0]=coor[0]+10
        return coor
if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([alto,ancho])
    a=pan_car([50,50],origen)
    b=pan_car([150,150],origen)
    c=pan_car([150,50],origen)
    plano(ventana)
    triangulo(ventana,a,b,c)

    lp=escalapuntofijo(c,2,a,b)
    pygame.draw.polygon(ventana,[255,255,255],lp,1)
    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            '''
            if event.type==pygame.KEYDOWN:

                a=trasl(a,event.key)
                b=trasl(b,event.key)
                c=trasl(c,event.key)
                ventana.fill([0,0,0])
                plano(ventana)
                triangulo(ventana,a,b,c)
            '''




        pygame.display.flip()
