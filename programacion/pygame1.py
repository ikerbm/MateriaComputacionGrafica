
import pygame
alto=500
ancho=700
pygame.init()
ventana=pygame.display.set_mode([ancho,alto])
y=200
x=100

fin=False
while not fin:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            fin=True

        if event.type == pygame.KEYDOWN:
            print event.key
            if event.key ==pygame.K_DOWN:
                y+=5
            if event.key ==pygame.K_UP:
                y-=5
            if event.key ==pygame.K_RIGHT:
                x+=5
            if event.key ==pygame.K_LEFT:
                x-=5
    ventana.fill([0,0,0])
    pygame.draw.line(ventana,[255,255,0],[x,y],[x+200,y],2)
    pygame.draw.line(ventana,[255,255,0],[x,y],[x+100,y+100],2)
    pygame.draw.line(ventana,[255,255,0],[x+200,y],[x+100,y+100],2)
    pygame.display.flip()
