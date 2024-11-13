import pygame
import math
ancho=800
alto=600
amarillo=[255,255,0]
origen=[400,300]


def trans(coor,origen):
    return [coor[0]+origen[0],-coor[1]+origen[1]]

if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])


    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
