import pygame
from lib.grafica import *


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    ls=[[20,80], [100,80]]

    #1) establecer tralacion basado en pto fijo
    P=[20,80]
    T=[-20,-80]

    #2) Trasladar al origen los puntos usanto T
    ls_t=[]
    for p in ls:
        pt=Trasladar(p,T)
        ls_t.append(pt)

    #3) Escalar S=[2,2]
    S=[2,2]
    ls_e=[]
    for p in ls_t:
        pe=Escala(p,S)
        ls_e.append(pe)

    #4) Trasladamos con T=P
    T=P
    ls_ef=[]
    for p in ls_e:
        pef=Trasladar(p,T)
        ls_ef.append(pef)

    #Escalamiento normal
    ls_en=[]
    for p in ls:
        pe=Escala(p,S)
        ls_en.append(pe)

    pygame.draw.line(pantalla,AMARILLO,ls_ef[0],ls_ef[1],3)
    pygame.draw.line(pantalla,BLANCO,ls[0],ls[1],1)
    pygame.draw.line(pantalla,VERDE,ls_t[0],ls_t[1],1)
    pygame.draw.line(pantalla,AMARILLO,ls_e[0],ls_e[1],3)
    #pygame.draw.line(pantalla,AMARILLO,ls_ef[0],ls_ef[1],3)
    pygame.draw.line(pantalla,BLANCO,ls_en[0],ls_en[1],3)

    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
