import pygame
ancho=700
alto=600

def punto(v,pos,boton):
    color=250

    if boton==3:
        color=0
    else:
        color=250
    pygame.draw.circle(v,[255,color,0],pos,2,1)
    pygame.display.flip()


pygame.init()
ventana=pygame.display.set_mode([ancho,alto])

fin=False
while not fin:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        fin=True
    if event.type==pygame.MOUSEBUTTONDOWN:
        print event.pos, event.button
        np=list(event.pos)
        punto(ventana,np,event.button)
