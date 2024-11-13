import pygame

ANCHO = 1200
ALTO=700

VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def Punto(v,coor):
    pygame.draw.circle(v,ROJO,coor,5)
    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO,ALTO])

    centro=[300,500]
    y=centro[1]
    p_ini=[0,y]
    p_fin=[ALTO,y]
    pygame.draw.line(pantalla,BLANCO,p_ini,p_fin,1)
    x=centro[0]
    p_ini=[0,x]
    p_fin=[ANCHO,x]
    pygame.draw.line(pantalla,BLANCO,p_ini,p_fin,1)

    pygame.display.flip()
    p=(20,-20)
    px=centro[0]+p[0]
    py=centro[1]-p[1]
    Punto(pantalla,[px,py])
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:
