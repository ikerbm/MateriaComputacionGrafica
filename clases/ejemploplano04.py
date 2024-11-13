import pygame
from lib.grafica import *


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[500,350]
    p=[100,120]
    a=0
    reloj=pygame.time.Clock()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        #animacion
        pr=Rotacion(p,a)
        pantalla=Plano(pantalla,centro)
        pantalla=Punto(pantalla,p)
        pantalla=Punto(pantalla,pr, VERDE)

        pc=TrCart_Pant(centro,pr)
        pantalla=Punto(pantalla,pc, VERDE)
        pygame.display.flip()
        a+=5
        reloj.tick(10)

    pygame.quit()
