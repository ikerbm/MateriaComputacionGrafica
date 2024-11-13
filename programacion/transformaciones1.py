import pygame
from libreria import*
ancho=600
alto=800
blanco=[255,255,255]


def puntos(v):
    pygame.draw.circle(v,blanco,[500,200],1)
    pygame.draw.circle(v,blanco,[300,250],1)
    pygame.draw.circle(v,blanco,[500,350],1)
    pygame.draw.circle(v,blanco,[300,400],1)





if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([alto,ancho])

    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            plano(ventana)
            puntos(ventana)


        pygame.display.flip()
