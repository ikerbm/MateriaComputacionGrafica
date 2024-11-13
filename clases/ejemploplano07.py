import pygame
from lib.grafica import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    ls=[[20,80], [100,80]]

    for p in ls:
        pantalla=Punto(pantalla,p)

    T=[-20,-80]
    ls_t=[]
    for p in ls:
        pt=Trasladar(p,T)
        pantalla=Punto(pantalla,pt,VERDE)
        ls_t.append(pt)

    #linea
    pygame.draw.line(pantalla,BLANCO,ls[0],ls[1],1)
    pygame.draw.line(pantalla,VERDE,ls_t[0],ls_t[1],2)
    pygame.display.flip()


    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

    pygame.quit()
