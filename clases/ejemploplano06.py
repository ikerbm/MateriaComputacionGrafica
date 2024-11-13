import pygame
from lib.grafica import *


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[500,350]

    ls=[[100,120], [200,120], [150,180]]
    a=0
    pantalla=Plano(pantalla,centro)
    reloj=pygame.time.Clock()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

        #Aplica rotacion a elementos de la lista
        ls_r=[]
        for p in ls:
            pr=Rotacion(p,a)
            ls_r.append(pr)

        #Aplicar transformacion a cartesiano
        ls_c=[]
        for p in ls_r:
            pc=TrCart_Pant(centro,p)
            ls_c.append(pc)

        pygame.draw.polygon(pantalla,BLANCO,ls,1)
        pygame.draw.polygon(pantalla,VERDE,ls_r,1)
        pygame.draw.polygon(pantalla,VERDE,ls_c,1)
        pygame.display.flip()
        a+=5
        reloj.tick(10)

    pygame.quit()
