import pygame
from libreria import*
import math
pix=80
giro=30
escala=0.5
origeni=[400,500]
def planoiso(ventana):
    pygame.draw.line(ventana,blanco,origeni,[0,500])
    pygame.draw.line(ventana,blanco,origeni,[ancho,500])
    pygame.draw.line(ventana,blanco,origeni,[ancho/2,0])
    pygame.draw.line(ventana,blanco,origeni,[ancho/2,alto])

def ecuacion():
    a=[origeni[0]+3*pix,origeni[1]]
    af=drotapunfi(origeni,a,30)
    b=[af[0],af[1]-2*pix]
    c=[origeni[0],origeni[1]-pix]
    d=[c[0]+pix,c[1]]
    df=drotapunfi(c,d,30)
    e=[df[0],df[1]-pix]
    f=[e[0]+pix,e[1]]
    ff=drotapunfi(e,f,30)
    g=[b[0],b[1]-pix]
    gf=drotapunfi(b,g,20)
    h=[ff[0],ff[1]-pix]
    hf=drotapunfi(ff,h,20)
    j=[origeni[0]-3*pix,origeni[1]]
    jf=irotapunfi(origeni,j,30)
    k=[jf[0],jf[1]-pix]
    l=[df[0]-3*pix,df[1]]
    lf=irotapunfi(df,l,30)
    m=[lf[0],lf[1]-pix]
    n=[m[0]+pix,m[1]]
    nf=irotapunfi(m,n,30)
    o=[n[0],n[1]-pix]
    of=irotapunfi(nf,o,32)
    p=[of[0],of[1]+0.7*pix]
    q=[of[0]-pix,of[1]]
    qf=irotapunfi(of,q,30)
    i=[gf[0]-2.5*pix,gf[1]]
    ifi=irotapunfi(gf,i,30)
    return[af,b,c,df,e,ff,gf,hf,ifi,jf,k,lf,m,nf,of,p,qf]
def dibujar(v,coors):
    l1=[coors[10],coors[2],coors[3],coors[11]]
    l2=[coors[15],coors[13],coors[4],coors[5]]
    l3=[coors[8],coors[16],coors[7],coors[6]]
    l4=[coors[16],coors[12],coors[13],coors[14]]
    l5=[coors[1],coors[6],coors[7],coors[5]]
    pygame.draw.polygon(v,verde,l1)
    pygame.draw.polygon(v,verde,l2)
    pygame.draw.polygon(v,verde,l3)
    pygame.draw.polygon(v,verde,l4)
    pygame.draw.polygon(v,verde,l5)
    pygame.draw.line(v,rojo,origeni,coors[0])
    pygame.draw.line(v,rojo,coors[0],coors[1])
    pygame.draw.line(v,rojo,origeni,coors[2])
    pygame.draw.line(v,rojo,coors[2],coors[3])
    pygame.draw.line(v,rojo,coors[3],coors[4])
    pygame.draw.line(v,rojo,coors[4],coors[1])
    pygame.draw.line(v,rojo,coors[1],coors[6])
    pygame.draw.line(v,rojo,coors[5],coors[7])
    pygame.draw.line(v,rojo,coors[6],coors[7])
    pygame.draw.line(v,rojo,origeni,coors[9])
    pygame.draw.line(v,rojo,coors[9],coors[10])
    pygame.draw.line(v,rojo,coors[10],coors[2])
    pygame.draw.line(v,rojo,coors[11],coors[3])
    pygame.draw.line(v,rojo,coors[11],coors[10])
    pygame.draw.line(v,rojo,coors[11],coors[12])
    pygame.draw.line(v,rojo,coors[12],coors[4])
    pygame.draw.line(v,rojo,coors[13],coors[14])
    pygame.draw.line(v,rojo,coors[15],coors[13])
    pygame.draw.line(v,rojo,coors[14],coors[15])
    pygame.draw.line(v,rojo,coors[15],coors[5])
    pygame.draw.line(v,rojo,coors[14],coors[16])
    pygame.draw.line(v,rojo,coors[16],coors[12])
    pygame.draw.line(v,rojo,coors[7],coors[14])
    pygame.draw.line(v,rojo,coors[8],coors[6])
    pygame.draw.line(v,rojo,coors[8],coors[16])




if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    planoiso(ventana)
    lista=ecuacion()
    dibujar(ventana,lista)
    fin=False
    lista2=lista
    i=0
    #escalamos la lista con coordenadas estandar
    
    for elem in lista:
        lista2[i]=escalapuntofijo(origeni,0.5,elem)
        i+=1
    lista3=lista2
    i=0
    #rotamos la lista con las coordenadas escaladas
    for elem in lista2:
        lista3[i]=rotacionpuntofijo(origeni,30,elem)
        i+=1


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                ventana.fill(negro)
                planoiso(ventana)
                dibujar(ventana,lista3)



        pygame.display.flip()
