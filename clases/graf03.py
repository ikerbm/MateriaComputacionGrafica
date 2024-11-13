import pygame

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([800,600])
    fin=False
    pos_x=200
    pos_y=200
    acex=0
    acey=0
    reloj=pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    acex= -6
                    acey=0
                if event.key==pygame.K_d:
                    acex= 6
                    acey=0
                if event.key==pygame.K_w:
                    acey= -6
                    acex=0
                if event.key==pygame.K_s:
                    acey= 6
                    acex=0
        pos_x+=acex
        pos_y+=acey
        pos=[pos_x,pos_y]
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[0,255,0],pos,10)
        pygame.display.flip()
        reloj.tick(30)
