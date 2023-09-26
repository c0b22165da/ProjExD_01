import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_gyaku=pg.transform.flip(bg_img,True,False)
    koukaton=pg.image.load("ex01/fig/3.png")
    koukaton_gyaku=pg.transform.flip(koukaton,True,False)
    koukaton_kaiten=pg.transform.rotozoom(koukaton_gyaku,10,1.0)
    koukaton_kaiten2=pg.transform.rotozoom(koukaton_gyaku,1,1.0)
    koukaton_kaiten3=pg.transform.rotozoom(koukaton_gyaku,3,1.0)
    koukaton_kaiten5=pg.transform.rotozoom(koukaton_gyaku,5,1.0)
    koukaton_kaiten7=pg.transform.rotozoom(koukaton_gyaku,7,1.0)
    
    tmr = 0
    x=0
    koukatonl=[koukaton_gyaku,koukaton_kaiten2,koukaton_kaiten3,koukaton_kaiten5,koukaton_kaiten7,koukaton_kaiten]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [1600-(x+1600)%3200, 0])
        screen.blit(bg_img_gyaku,[1600-x%3200,0])
        screen.blit(koukatonl[tmr%6],[300,200])
        pg.display.update()
        tmr += 1  
        x+=1
        clock.tick(400)
    



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()