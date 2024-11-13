import pygame
from libreria import*
alto1=300
ancho1=900
origen1=[1,alto1-1]
origen2=[1+(ancho1/3),alto1-1]
origen3=[1+(2*ancho1/3),alto1-2]
pix=95
def plano3(v):
    pygame.draw.line(v,blanco,[ancho1/3,0],[ancho1/3,alto1])
    pygame.draw.line(v,blanco,[2*ancho1/3,0],[2*ancho1/3,alto1])
    pygame.draw.line(v,blanco,[ancho1,0],[ancho1,alto1])
def planta(v):
    a=[origen1[0]+pix*3,origen1[1]]
    pygame.draw.line(v,rojo,origen1,a)
    b=[a[0],a[1]-pix*3]
    pygame.draw.line(v,rojo,a,b)
    c=[origen1[0],origen1[1]-pix]
    pygame.draw.line(v,rojo,origen1,c)
    d=[c[0]+pix,c[1]]
    pygame.draw.line(v,rojo,c,d)
    e=[d[0],d[1]-pix]
    pygame.draw.line(v,rojo,d,e)
    f=[e[0]+2*pix,e[1]]
    pygame.draw.line(v,rojo,e,f)
    g=[b[0]-pix,b[1]]
    pygame.draw.line(v,rojo,b,g)
    h=[g[0],g[1]+pix]
    pygame.draw.line(v,rojo,g,h)
    pygame.draw.line(v,rojo,g,e)
def perfil(v):
    a=[origen2[0]+pix*3,origen2[1]]
    b=[a[0],a[1]-2*pix]
    pygame.draw.line(v,morado,origen2,a)
    pygame.draw.line(v,morado,a,b)
    c=[origen2[0],origen2[1]-pix]
    d=[c[0],c[1]-pix]
    e=[d[0],d[1]-pix]
    pygame.draw.line(v,morado,origen2,c)
    pygame.draw.line(v,morado,c,d)
    pygame.draw.line(v,morado,d,e)
    pygame.draw.line(v,morado,d,b)
    f=[c[0]+3*pix,c[1]]
    pygame.draw.line(v,morado,c,f)
    g=[e[0]+pix,e[1]]
    h=[g[0]+pix,g[1]]
    i=[g[0],g[1]+pix]
    pygame.draw.line(v,morado,e,g)
    pygame.draw.line(v,morado,g,h)
    pygame.draw.line(v,morado,g,i)
    pygame.draw.line(v,morado,h,b)
def alzado(v):
    a=[origen3[0],origen[1]-pix]
    b=[a[0],a[1]-pix]
    c=[b[0],b[1]-pix]
    d=[c[0]+2*pix,c[1]]
    e=[d[0]+pix,d[1]]
    f=[e[0],e[1]+pix]
    g=[f[0],f[1]+pix]
    h=[g[0],g[1]+pix-1]
    lista=[origen3,a,b,c,d,e,f,g,h]
    pygame.draw.polygon(v,azul,lista,1)
    i=[d[0],d[1]+pix]
    j=[b[0]+pix,b[1]]
    k=[j[0],j[1]+pix]
    pygame.draw.line(v,azul,b,f)
    pygame.draw.line(v,azul,d,i)
    pygame.draw.line(v,azul,j,k)
    pygame.draw.line(v,azul,a,g)


if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho1,alto1])
    
    planta(ventana)
    perfil(ventana)
    alzado(ventana)
    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pygame.display.flip()
