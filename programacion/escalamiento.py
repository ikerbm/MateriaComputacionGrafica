import pygame
from libreria import*
def triangulo(v,a,b,c):
    pygame.draw.line(ventana,[255,0,0],a,b)
    pygame.draw.line(ventana,[255,0,0],c,b)
    pygame.draw.line(ventana,[255,0,0],a,c)

if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([alto,ancho])
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            a=[150,100]
            b=[300,100]
            c=[150,200]
            triangulo(ventana,a,b,c)
            q=escalar(a,2)
            w=escalar(b,2)
            e=escalar(c,2)
            triangulo(ventana,q,w,e)
            q=escalar(a,0.5)
            w=escalar(b,0.5)
            e=escalar(c,0.5)
            triangulo(ventana,q,w,e)


        pygame.display.flip()
