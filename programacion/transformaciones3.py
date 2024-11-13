import pygame
from libreria import*
blanco=[255,255,255]
amarillo=[255,255,0]
ancho=800
alto=600
origen=[400,300]



def puntos(v,pos):
    pygame.draw.circle(v,[255,255,0],pos,2,1)



def linea(v,lp):
    pygame.draw.line(v,amarillo,lp[0],lp[1])


if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    p=0
    lp=[]
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            plano(ventana)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.pos
                puntos(ventana,event.pos)
                coor2=pan_car(event.pos,origen)
                lp.append(event.pos)
                p=p+1
                if(p==2):
                    linea(ventana,lp)









        pygame.display.flip()
