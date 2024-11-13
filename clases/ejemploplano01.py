import pygame
from lib.grafica import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[400,500]
    pantalla=Plano(pantalla,centro)
    ls=[ [100,100], [-100,100], [-100,0] ]

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.pos
                centro=event.pos

        ls_cart=[]
        for p in ls:
            p_cart = TrCart_Pant(centro,p)
            ls_cart.append(p_cart)

        pantalla.fill(NEGRO)
        pantalla=Plano(pantalla,centro)
        pygame.draw.polygon(pantalla,VERDE,ls,1)
        pygame.draw.polygon(pantalla,VERDE,ls_cart,1)
        pygame.display.flip()
