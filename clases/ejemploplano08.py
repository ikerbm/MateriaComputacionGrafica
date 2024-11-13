import pygame
from lib.grafica import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    ls=[[20,80], [100,80]]
    T=[0,0]
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    T[0]+=5
                if event.key == pygame.K_LEFT:
                    T[0]-=5

        #linea
        for p in ls:
            pantalla=Punto(pantalla,p)

        ls_t=[]
        for p in ls:
            pt=Trasladar(p,T)
            ls_t.append(pt)

        pantalla.fill(NEGRO)
        pygame.draw.line(pantalla,BLANCO,ls[0],ls[1],1)
        pygame.draw.line(pantalla,VERDE,ls_t[0],ls_t[1],1)

        pygame.display.flip()

    pygame.quit()
