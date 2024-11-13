import pygame
import math
ANCHO=800
ALTO=800
CENTRO=[ANCHO/2,ALTO/2]
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
AMARILLO=[200,200,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
PUNTO1=[0,400]
PUNTO2=[800,400]
PUNTO3=[400,0]
PUNTO4=[400,800]
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

def cuadro(v,lcor, color):
    pygame.draw.polygon(v,color,lcor,2)

def TrCart_Pant(c,p):
    px=c[0]+p[0]
    py=c[1]-p[1]
    return [px,py]

def Rotacion(p,a):
    ar=math.radians(a)
    xp= (p[0]*math.cos(ar)) + (p[1]*math.sin(ar))
    yp= -(p[0]*math.sin(ar)) + (p[1]*math.cos(ar))
    return [int(xp), int(yp)]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin=False

    reloj=pygame.time.Clock()
#definicion de variables
    angulo=0
    anguloi=0
    angulod=0
    anguloa=0
    angulob=0
    #coordenadas iniciales del cuadrado VERDE de como queremos que se vea en cartesiano
    p1=[200,200]
    p2=[200,-200]
    p3=[-200,-200]
    p4=[-200,200]
    p5=[400,400]
    p6=[400,-400]
    p7=[-400,-400]
    p8=[-400,400]
    #conversion de lass coordenadas iniciales del cuadrado VERDE a coordenadas en pantalla
    p1c=TrCart_Pant(CENTRO,p1)
    p2c=TrCart_Pant(CENTRO,p2)
    p3c=TrCart_Pant(CENTRO,p3)
    p4c=TrCart_Pant(CENTRO,p4)
    p5c=TrCart_Pant(CENTRO,p5)
    p6c=TrCart_Pant(CENTRO,p6)
    p7c=TrCart_Pant(CENTRO,p7)
    p8c=TrCart_Pant(CENTRO,p8)
    lcor=[p1c,p2c,p3c,p4c]



    while not fin:

        #cuadrado VERDE
        angulo+=1
        pr1=Rotacion(p1,angulo)
        pr2=Rotacion(p2,angulo)
        pr3=Rotacion(p3,angulo)
        pr4=Rotacion(p4,angulo)
        p1ro=TrCart_Pant(CENTRO,pr1)
        p2ro=TrCart_Pant(CENTRO,pr2)
        p3ro=TrCart_Pant(CENTRO,pr3)
        p4ro=TrCart_Pant(CENTRO,pr4)
        pr5=Rotacion(p5,angulo)
        pr6=Rotacion(p6,angulo)
        pr7=Rotacion(p7,angulo)
        pr8=Rotacion(p8,angulo)
        p5ro=TrCart_Pant(CENTRO,pr5)
        p6ro=TrCart_Pant(CENTRO,pr6)
        p7ro=TrCart_Pant(CENTRO,pr7)
        p8ro=TrCart_Pant(CENTRO,pr8)
        lcorr=[p1ro,p2ro,p3ro,p4ro]
        #cuadrado ROJO
        anguloi-=1
        p1i=Rotacion(p1,anguloi)
        p2i=Rotacion(p2,anguloi)
        p3i=Rotacion(p3,anguloi)
        p4i=Rotacion(p4,anguloi)
        p5i=Rotacion(p5,anguloi)
        p6i=Rotacion(p6,anguloi)
        p7i=Rotacion(p7,anguloi)
        p8i=Rotacion(p8,anguloi)
        p1ir=TrCart_Pant(PUNTO1,p1i)
        p2ir=TrCart_Pant(PUNTO1,p2i)
        p3ir=TrCart_Pant(PUNTO1,p3i)
        p4ir=TrCart_Pant(PUNTO1,p4i)
        p5ir=TrCart_Pant(PUNTO1,p5i)
        p6ir=TrCart_Pant(PUNTO1,p6i)
        p7ir=TrCart_Pant(PUNTO1,p7i)
        p8ir=TrCart_Pant(PUNTO1,p8i)
        lcori=[p1ir,p2ir,p3ir,p4ir]
        angulod+=1
        p1d=Rotacion(p1,angulod)
        p2d=Rotacion(p2,angulod)
        p3d=Rotacion(p3,angulod)
        p4d=Rotacion(p4,angulod)
        p5d=Rotacion(p5,angulod)
        p6d=Rotacion(p6,angulod)
        p7d=Rotacion(p7,angulod)
        p8d=Rotacion(p8,angulod)
        p1dr=TrCart_Pant(PUNTO2,p1d)
        p2dr=TrCart_Pant(PUNTO2,p2d)
        p3dr=TrCart_Pant(PUNTO2,p3d)
        p4dr=TrCart_Pant(PUNTO2,p4d)
        p5dr=TrCart_Pant(PUNTO2,p5d)
        p6dr=TrCart_Pant(PUNTO2,p6d)
        p7dr=TrCart_Pant(PUNTO2,p7d)
        p8dr=TrCart_Pant(PUNTO2,p8d)
        lcord=[p1dr,p2dr,p3dr,p4dr]
        #cuadrado AZUL
        anguloa+=1
        p1a=Rotacion(p1,anguloa)
        p2a=Rotacion(p2,anguloa)
        p3a=Rotacion(p3,anguloa)
        p4a=Rotacion(p4,anguloa)
        p5a=Rotacion(p5,anguloa)
        p6a=Rotacion(p6,anguloa)
        p7a=Rotacion(p7,anguloa)
        p8a=Rotacion(p8,anguloa)
        p1ar=TrCart_Pant(PUNTO3,p1a)
        p2ar=TrCart_Pant(PUNTO3,p2a)
        p3ar=TrCart_Pant(PUNTO3,p3a)
        p4ar=TrCart_Pant(PUNTO3,p4a)
        p5ar=TrCart_Pant(PUNTO3,p5a)
        p6ar=TrCart_Pant(PUNTO3,p6a)
        p7ar=TrCart_Pant(PUNTO3,p7a)
        p8ar=TrCart_Pant(PUNTO3,p8a)
        lcora=[p1ar,p2ar,p3ar,p4ar]
        angulob-=1
        p1b=Rotacion(p1,angulob)
        p2b=Rotacion(p2,angulob)
        p3b=Rotacion(p3,angulob)
        p4b=Rotacion(p4,angulob)
        p5b=Rotacion(p5,angulob)
        p6b=Rotacion(p6,angulob)
        p7b=Rotacion(p7,angulob)
        p8b=Rotacion(p8,angulob)
        p1br=TrCart_Pant(PUNTO4,p1b)
        p2br=TrCart_Pant(PUNTO4,p2b)
        p3br=TrCart_Pant(PUNTO4,p3b)
        p4br=TrCart_Pant(PUNTO4,p4b)
        p5br=TrCart_Pant(PUNTO4,p5b)
        p6br=TrCart_Pant(PUNTO4,p6b)
        p7br=TrCart_Pant(PUNTO4,p7b)
        p8br=TrCart_Pant(PUNTO4,p8b)
        lcorb=[p1br,p2br,p3br,p4br]

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin=True

        #actualizaciones
        pantalla.fill(NEGRO)
        cuadro(pantalla,lcorr,VERDE)
        pygame.draw.line(pantalla,VERDE,p1ro,p5ro,2)
        pygame.draw.line(pantalla,VERDE,p2ro,p6ro,2)
        pygame.draw.line(pantalla,VERDE,p3ro,p7ro,2)
        pygame.draw.line(pantalla,VERDE,p4ro,p8ro,2)
        if(p1ir[0]>=0):
            pygame.draw.line(pantalla,ROJO,p1ir,p4dr,2)
        if(p2ir[0]>=0):
            pygame.draw.line(pantalla,ROJO,p2ir,p3dr,2)
        if(p3ir[0]>=0):
            pygame.draw.line(pantalla,ROJO,p3ir,p2dr,2)
        if(p4ir[0]>=0):
            pygame.draw.line(pantalla,ROJO,p4ir,p1dr,2)
        pygame.draw.polygon(pantalla,ROJO,lcori,2)
        pygame.draw.polygon(pantalla,ROJO,lcord,2)

        if(p1ar[1]>=0):
            pygame.draw.line(pantalla,AZUL,p1ar,p2br,2)
        if(p2ar[1]>=0):
            pygame.draw.line(pantalla,AZUL,p2ar,p1br,2)
        if(p3ar[1]>=0):
            pygame.draw.line(pantalla,AZUL,p3ar,p4br,2)
        if(p4ar[1]>=0):
            pygame.draw.line(pantalla,AZUL,p4ar,p3br,2)

        pygame.draw.polygon(pantalla,AZUL,lcora,2)
        pygame.draw.polygon(pantalla,AZUL,lcorb,2)
        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()
