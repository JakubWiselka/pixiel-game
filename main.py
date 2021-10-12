from materials import dirt, water, sand
import pygame
import numpy as np
import time
import math

GAME_SIZE = (100, 50, 10)
COL_BACKGROUND = (10, 10, 40)
COL_GRID = (30, 30, 60)
PEN_SIZE = ()

COL_SOLID = (5, 5, 5)       # 1
COL_WATER = (0,0,200)       # 2
COL_DIRT = (155, 118, 83)   # 3
COL_SAND = (194, 178, 128)  # 4

GAME_TICK = 0.0250

SETTINGS = {
    'pause': False,
}

def update(surface, cur, sz):
    nxt = init(cur.shape[1], cur.shape[0])

    for r, c in np.ndindex(cur.shape):
        this = cur[r, c]
        if not this:
            col = COL_BACKGROUND
        elif this == 2:
            dirt(nxt, this, r, c, cur)
            col = COL_DIRT
        elif this == 3:
            water(nxt, this, r, c, cur)
            col = COL_WATER
        elif this == 4:
            sand(nxt, this, r, c, cur)
            col = COL_SAND
        elif this == 1:
            nxt[r, c] = 1
            col = COL_SOLID

        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def init(dimx, dimy):
    cells = np.zeros((dimy-1, dimx))
    cells = np.append(cells, np.ones((1, dimx)), axis=0)
    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("PIXEL GAME")

    cells = init(dimx, dimy)
    tick = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # PAUSE GAME
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                SETTINGS['pause'] = False if SETTINGS['pause'] else True
            # CLEAR GAME
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                cells = init(dimx, dimy)
            # MOUSE EVENTS
            if any(pygame.mouse.get_pressed()):
                mouse = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                col = math.floor(pos[0]/GAME_SIZE[2])
                row = math.floor(pos[1]/GAME_SIZE[2])
                if mouse[0]:
                    cells[row][col] = 2
                    color = COL_DIRT
                if mouse[2]:
                    cells[row][col] = 3
                    color = COL_WATER
                if mouse[1]:
                    cells[row][col] = 4
                    color = COL_SOLID
                pygame.draw.rect(surface, color, (col*cellsize, row*cellsize, cellsize-1, cellsize-1))
                

        if not SETTINGS['pause'] and (time.time() - tick) > GAME_TICK:
            tick = time.time()
            surface.fill(COL_GRID)
            cells = update(surface, cells, cellsize)
            pygame.display.update()

        
if __name__ == "__main__":
    dimx, dimy, cellsize = GAME_SIZE
    main(dimx, dimy, cellsize)
