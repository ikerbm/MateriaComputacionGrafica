import pygame
import math

ANCHO=1200
ALTO=700

#Lista de colores
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
AMARILLO=[200,200,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def Punto(p,pos,cl=BLANCO):
    pygame.draw.circle(p,cl,pos,2)
    return p

def Rotacion(p,a):
    ar=math.radians(a)
    xp= (p[0]*math.cos(ar)) + (p[1]*math.sin(ar))
    yp= -(p[0]*math.sin(ar)) + (p[1]*math.cos(ar))
    return [int(xp), int(yp)]

def Plano(p,c):
    centro=c
    y=centro[1]
    p_ini=[0,y]
    p_fin=[ANCHO,y]
    pygame.draw.line(p,BLANCO,p_ini,p_fin,1)
    x=centro[0]
    p_ini=[x,0]
    p_fin=[x,ALTO]
    pygame.draw.line(p,BLANCO,p_ini,p_fin,1)
    return p

def TrCart_Pant(c,p):
    px=c[0]+p[0]
    py=c[1]-p[1]
    return [px,py]

def Trasladar(p,T):
    xp=p[0]+T[0]
    yp=p[1]+T[1]
    return [xp,yp]

def Escala(p,s):
    xp=p[0]*s[0]
    yp=p[1]*s[1]
    return [xp,yp]

def Polar_cart(p):
    r=p[0]
    a=p[1]
    ar=math.radians(a)
    x= r * math.cos(ar)
    y= r * math.sin(ar)
    return [int(x),int(y)]
