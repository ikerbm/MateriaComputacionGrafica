import math
import pygame
blanco=[255,255,255]
ancho=800
alto=600
origen=[400,300]
def plano(v):
    pygame.draw.line(v,blanco,[400,300],[0,300])
    pygame.draw.line(v,blanco,[400,300],[800,300])
    pygame.draw.line(v,blanco,[400,300],[400,0])
    pygame.draw.line(v,blanco,[400,300],[400,600])
def trans(coor):
    return[coor[0]+origen[0],-coor[1]+origen[1]]
def punto(coor):
    pygame.draw.circle(ventana,blanco,coor,1)


def horaria(coor,gr):
    gr=gr+1
    rad=math.radians(gr)
    xp=(coor[0]*math.cos(rad)) + (coor[1]*math.sin(rad))
    yp=(-1*coor[0]*math.sin(rad))+ (coor[1]*math.cos(rad))

if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    fin=False
    gr=0
    q=0
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            plano(ventana)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if q==0:
                    coor=list(event.pos)
                    punto(coor)
        pygame.display.flip()
