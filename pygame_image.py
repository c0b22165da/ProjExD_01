import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton=pg.image.load("ex01/fig/3.png")
    koukaton_gyaku=pg.transform.flip(koukaton,True,False)
    koukaton_kaiten=pg.transform.rotozoom(koukaton_gyaku,10,1.0)
    tmr = 0
    koukatonl=[koukaton_gyaku,koukaton_kaiten]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(koukatonl[tmr%2],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)
    



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()