import pygame
ANCHO = 1200
ALTO=700

VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def Punto(coor):
    pygame.draw.circle(pantalla,ROJO,coor,5)
    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO,ALTO])

    pygame.draw.circle(pantalla,VERDE,[100,100],5)
    pygame.display.flip()

    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                coor=event.pos
                Punto(coor)
