import pygame
from lib.grafica import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[600,400]

    ls=[ [100,100], [300,100], [100,50] ]
    ls_cart=[]
    for p in ls:
        p_cart = TrCart_Pant(centro,p)
        ls_cart.append(p_cart)
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ls_aux=[]
                    for p in ls:
                        p[0]= p[0] - 400
                        p_cart = TrCart_Pant(centro,p)
                        ls_aux.append(p_cart)
                    ls_cart=ls_aux

        pantalla=Plano(pantalla,centro)
        pygame.draw.polygon(pantalla,VERDE,ls,1)
        pygame.draw.polygon(pantalla,VERDE,ls_cart,1)
        pygame.display.flip()
