import pygame
from lib.grafica import *


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[350,300]
    n=3
    amp=360/n
    r=100
    val_r=90

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        ls_f=[]
        for i in range(n):
            angulo=i*amp
            #Coordena polar
            p=[r,angulo+val_r]
            polar=Polar_cart(p)
            print angulo, polar
            ls_f.append(polar)

        ls_c=[]
        for p in ls_f:
            p=TrCart_Pant(centro,p)
            ls_c.append(p)

        pygame.draw.polygon(pantalla,BLANCO,ls_f,1)
        pygame.draw.polygon(pantalla,BLANCO,ls_c,1)
        pantalla=Plano(pantalla,centro)

        pygame.display.flip()
