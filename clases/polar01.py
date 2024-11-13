import pygame
from lib.grafica import *


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[350,300]

    #Coordenada polar A=[r,a]
    a=0
    l=100
    n=3
    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        ar=math.radians(a)
        r=l * math.cos(n*ar)
        A=[r,a]
        p_pantalla=Polar_cart(A)
        pantalla=Punto(pantalla,p_pantalla)

        pc=TrCart_Pant(centro,p_pantalla)
        pantalla=Punto(pantalla,pc)
        pantalla=Plano(pantalla,centro)
        pygame.display.flip()
        a+=5
        reloj.tick(30)
