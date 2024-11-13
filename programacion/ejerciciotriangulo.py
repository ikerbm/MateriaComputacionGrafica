import pygame
ancho=800
alto=600
distancia1=0
distancia2=0
distancia3=0
lista=[]
coordenada=[]
pix=0

def triangulo(v,p):
    pygame.draw.line(v,[255,255,0],[p[0],p[1]],[p[0],p[1]+150],2)
    pygame.draw.line(v,[255,255,0],[p[0],p[1]+150],[p[0]+50,p[1]+100],2)
    pygame.draw.line(v,[255,255,0],[p[0],p[1]],[p[0]+50,p[1]+100],2)

def unificacion(v,p):
    pygame.draw.line(v,[255,0,0],p[0],p[1],2)
    pygame.draw.line(v,[255,0,0],[p[0][0],p[0][1]+150],[p[1][0],p[1][1]+150],2)
    pygame.draw.line(v,[255,0,0],[p[0][0]+50,p[0][1]+100],[p[1][0]+50,p[1][1]+100],2)

def tribal(v,pix):
    while pix <= 800:
        pygame.draw.line(v,[255,255,255],[pix,600-16],[pix+15,600-16])
        pygame.draw.line(v,[255,255,255],[pix+15,600-16],[pix+15,600-1])
        pygame.draw.line(v,[255,255,255],[pix+15,600-1],[pix,600-1])
        pygame.draw.line(v,[255,255,255],[pix,600-1],[pix,600-11])
        pygame.draw.line(v,[255,255,255],[pix,600-11],[pix+10,600-11])
        pygame.draw.line(v,[255,255,255],[pix+10,600-11],[pix+10,600-6])
        pygame.draw.line(v,[255,255,255],[pix+10,600-6],[pix+5,600-6])
        pix+=20



if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([800,600])

    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            tribal(ventana,pix)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.pos, event.button
                triangulo(ventana,list(event.pos))
                lista.append(list(event.pos))


           
       pygame.display.flip()
