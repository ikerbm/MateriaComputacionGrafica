import pygame
from libreria import*
ancho=600
alto=800
blanco=[255,255,255]
amarillo=[255,255,0]
origen=[400,300]


def dibujar(v,coor,coor2):
    pygame.draw.line(v,blanco,coor,coor2)

def triangulo(v,a,b,c):
    dibujar(v,a,b)
    dibujar(v,a,c)
    dibujar(v,b,c)

if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([alto,ancho])

    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            plano(ventana)
            a=[100,200]
            b=[350,200]
            c=[200,350]

            triangulo(ventana,a,b,c)
            ta=pan_car(a,origen)
            tb=pan_car(b,origen)
            tc=pan_car(c,origen)
            triangulo(ventana,ta,tb,tc)
            lp=[ta,tb,tc]




        pygame.display.flip()
