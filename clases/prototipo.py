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

def Trasladar(p,T):
    xp=p[0]+T[0]
    yp=p[1]+T[1]
    return [xp,yp]
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
        cuadro(pantalla,lcor,AZUL)

        Plano(pantalla,CENTRO)
        if(p1ar[1]>=0):
            pygame.draw.line(pantalla,VERDE,p1ar,p2br,2)
        if(p2ar[1]>=0):
            pygame.draw.line(pantalla,VERDE,p2ar,p1br,2)
        if(p3ar[1]>=0):
            pygame.draw.line(pantalla,VERDE,p3ar,p4br,2)
        if(p4ar[1]>=0):
            pygame.draw.line(pantalla,VERDE,p4ar,p3br,2)

        pygame.draw.polygon(pantalla,VERDE,lcora,2)
        pygame.draw.polygon(pantalla,VERDE,lcorb,2)
        #pygame.draw.polygon(pantalla,VERDE,lcord,2)
        '''
        pygame.draw.line(pantalla,VERDE,p1ir,p5ir,2)
        pygame.draw.line(pantalla,VERDE,p2ir,p6ir,2)
        pygame.draw.line(pantalla,VERDE,p3ir,p7ir,2)
        pygame.draw.line(pantalla,VERDE,p4ir,p8ir,2)

        pygame.draw.line(pantalla,VERDE,p1dr,p5dr,2)
        pygame.draw.line(pantalla,VERDE,p2dr,p6dr,2)
        pygame.draw.line(pantalla,VERDE,p3dr,p7dr,2)
        pygame.draw.line(pantalla,VERDE,p4dr,p8dr,2)
        '''
        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()
