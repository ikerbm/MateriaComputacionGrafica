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

def horaria(coor,gr):
    gr+=1
    rad=math.radians(gr)
    xp=(coor[0]*math.cos(rad)) + (coor[1]*math.sin(rad))
    yp=(-1*coor[0]*math.sin(rad))+ (coor[1]*math.cos(rad))

    return [int(xp),int(yp)]
def antihoraria(coor,gr):
    gr=gr-1
    rad=math.radians(gr)
    xp=(coor[0]*math.cos(rad)) + (-1*coor[1]*math.sin(rad))
    yp=(coor[0]*math.sin(rad))+ (coor[1]*math.cos(rad))

    return [int(xp),int(yp)]





if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    fin=False
    gr=0
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            plano(ventana)
            a=[100,50]
            b=[200,50]
            c=[200,100]
            at=trans(a)
            bt=trans(b)
            ct=trans(c)
            lt=[at,bt,ct]
            lr=lt
            lr1=lt
            pygame.draw.polygon(ventana,blanco,lt,1)
            if event.type==pygame.KEYDOWN:
                if event.key==276:
                    ar1=antihoraria(lr1[0],gr)
                    br1=antihoraria(lr1[1],gr)
                    cr1=antihoraria(lr1[2],gr)

                    ventana.fill([0,0,0])
                    plano(ventana)
                    pygame.draw.polygon(ventana,blanco,[ar1,br1,cr1],1)
                if event.key==275:
                    ar=horaria(lr[0],gr)
                    br=horaria(lr[1],gr)
                    cr=horaria(lr[2],gr)

                    ventana.fill([0,0,0])
                    plano(ventana)
                    pygame.draw.polygon(ventana,blanco,[ar,br,cr],1)


        pygame.display.flip()
