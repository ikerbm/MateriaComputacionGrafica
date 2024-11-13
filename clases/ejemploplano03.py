import pygame
from lib.grafica import *



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    ls=[ [100,60], [200,60], [200,90] ]
    S=[2,2]

    ls_e=[]
    for p in ls:
        pe=Escala(p,S)
        ls_e.append(pe)

    print ls_e
    pygame.draw.polygon(pantalla,BLANCO,ls,1)
    pygame.draw.polygon(pantalla,VERDE,ls_e,1)
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

    pygame.quit()
