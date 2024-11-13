import pygame
import math
#ventana
alto=600
ancho=800
origen=[ancho/2,alto/2]
#colores
blanco=[255,255,255]
amarillo=[255,255,0]
rojo=[255,0,0]
azul=[0,0,255]
verde=[0,128,0]
morado=[87,35,100]
negro=[0,0,0]
#dibujar un plano
def plano(ventana):
    pygame.draw.line(ventana,blanco,origen,[0,alto/2])
    pygame.draw.line(ventana,blanco,origen,[ancho,alto/2])
    pygame.draw.line(ventana,blanco,origen,[ancho/2,0])
    pygame.draw.line(ventana,blanco,origen,[ancho/2,alto])
#coordenada en pantalla -> coordenada cartesiana
def pan_car(coor,origen):
    return [coor[0]+origen[0],-coor[1]+origen[1]]
#rotacion de punto
def horaria(coor,grado):
    radian=math.radians(grado)
    xrotada=(coor[0]*math.cos(radian)) + (coor[1]*math.sin(radian))
    yrotada=(-1*coor[0]*math.sin(radian))+ (coor[1]*math.cos(radian))
    return [int(xrotada),int(yrotada)]

def antihoraria(coor,gr):
    gr=gr-1
    rad=math.radians(gr)
    xp=(coor[0]*math.cos(rad)) + (-1*coor[1]*math.sin(rad))
    yp=(coor[0]*math.sin(rad))+ (coor[1]*math.cos(rad))

    return [int(xp),int(yp)]

#escalamiento con punto fijo
def traslacion(coor,traslacion):
    #mueve los puntos a traslacion
    return [coor[0]+traslacion[0],coor[1]+traslacion[1]]
def restauracion(fijo,rest):
    return [rest[0]+fijo[0],rest[1]+fijo[1]]
def rotacionpuntofijo(puntofijo,rotacion,coor):
    tras=[puntofijo[0]*-1,puntofijo[1]*-1]
    fijo=puntofijo
    at=traslacion(puntofijo,tras)
    bt=traslacion(coor,tras)
    ar=horaria(at,rotacion)
    br=horaria(bt,rotacion)
    af=[ar[0]+fijo[0],ar[1]+fijo[1]]
    bf=[br[0]+fijo[0],br[1]+fijo[1]]
    return bf
def escalapuntofijo(puntofijo,escalamiento,coor):
    tras=[puntofijo[0]*-1,puntofijo[1]*-1]
    fijo=puntofijo
    at=traslacion(puntofijo,tras)
    bt=traslacion(coor,tras)
    ar=escalar(at,escalamiento)
    br=escalar(bt,escalamiento)
    af=[ar[0]+fijo[0],ar[1]+fijo[1]]
    bf=[br[0]+fijo[0],br[1]+fijo[1]]
    return bf
#escalamiento de un punto
def escalar(punto,escala):
    ls=[punto[0]*escala,punto[1]*escala]
    return ls
#hacer una cardioide, meter en un ciclo de 360
def cardioide(a,b,grados):
    radian=math.radians(grados)
    r=a+b*math.cos(radian)
    return r
#hacer una flor, b=cantidad de petalos, meter en ciclo de 360
def flor(a,b,g):
    rad=math.radians(g)
    r=a*math.cos(b*rad)
    return r
#de polar a pantalla
def polar_pan(r,grados):
    radian=math.radians(grados)
    x=r*math.cos(radian)
    y=r*math.sin(radian)
    lp=[x,y]
    return lp
def drotapunfi(puntofijo,coor,rotacion):
    t=[-1*puntofijo[0],-1*puntofijo[1]]
    coort=[t[0]+coor[0],t[1]+coor[1]]
    coorr=horaria(coort,rotacion)
    coorf=[coorr[0]+puntofijo[0],coorr[1]+puntofijo[1]]
    return coorf
def irotapunfi(puntofijo,coor,rotacion):
    t=[-1*puntofijo[0],-1*puntofijo[1]]
    coort=[t[0]+coor[0],t[1]+coor[1]]
    coorr=antihoraria(coort,rotacion)
    coorf=[coorr[0]+puntofijo[0],coorr[1]+puntofijo[1]]
    return coorf
