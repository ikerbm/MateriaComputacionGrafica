import pygame
ancho=800
alto=600
amarillo=[255,255,0]
origen=[400,300]
def triangulo(v,a,b,c):
    pygame.draw.line(ventana,[255,0,0],a,b)
    pygame.draw.line(ventana,[255,0,0],c,b)
    pygame.draw.line(ventana,[255,0,0],a,c)
def plano(v):
    pygame.draw.line(v,amarillo,origen,[0,300])
    pygame.draw.line(v,amarillo,origen,[ancho,300])
    pygame.draw.line(v,amarillo,origen,[400,0])
    pygame.draw.line(v,amarillo,origen,[400,alto])
def trans(coor,origen):
    return [coor[0]+origen[0],-coor[1]+origen[1]]
def trasl(coor,evento):
    if evento == 273:
        coor[1]=coor[1]-10
        return coor
    if evento == 274:
        coor[1]=coor[1]+10
        return coor
    if evento == 276:
        coor[0]=coor[0]-10
        return coor
    if evento == 275:
        coor[0]=coor[0]+10
        return coor
def traslacion(coor,tras):
    return [coor[0]+tras[0],coor[1]+tras[1]]
def espufi(a,esca,b,c):
    tras=[a[0]*-1,a[1]*-1]
    fijo=a
    at=traslacion(a,tras)
    bt=traslacion(b,tras)
    ct=traslacion(c,tras)
    ae=[at[0]*esca,at[1]*esca]
    be=[bt[0]*esca,bt[1]*esca]
    ce=[ct[0]*esca,ct[1]*esca]
    af=[ae[0]+fijo[0],ae[1]+fijo[1]]
    bf=[be[0]+fijo[0],be[1]+fijo[1]]
    cf=[ce[0]+fijo[0],ce[1]+fijo[1]]
    return [af,bf,cf]





if __name__ =='__main__':
    pygame.init()
    ventana=pygame.display.set_mode([ancho,alto])
    a=trans([50,50],origen)
    b=trans([150,150],origen)
    c=trans([150,50],origen)
    plano(ventana)
    triangulo(ventana,a,b,c)

    lp=espufi(c,2,a,b)
    pygame.draw.polygon(ventana,[255,255,255],lp,1)
    fin=False


    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            '''
            if event.type==pygame.KEYDOWN:

                a=trasl(a,event.key)
                b=trasl(b,event.key)
                c=trasl(c,event.key)
                ventana.fill([0,0,0])
                plano(ventana)
                triangulo(ventana,a,b,c)
            '''




        pygame.display.flip()
