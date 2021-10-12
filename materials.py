import random
import numpy as np

def dirt(nxt, this, r, c, cur):
    if not cur[r+1, c]:
        nxt[r, c] = 0
        nxt[r+1, c] = 2
    else:
        nxt[r, c] = 2

def water(nxt, this, r, c, cur):
    def _random_posible_direction(left, right, r, c, nxt):
        if left and right:
            weight = [0.05, 0.90, 0.05]
        elif left:
            weight = [0.05, 0.95, 0.00]
        else:
            weight = [0.00, 0.95, 0.05]
        res = np.random.choice([-1, 0, 1], 1, p = weight)
        if res[0]:
            nxt[r, c] = 0
            nxt[r, c + res] = 3
        else:
            nxt[r, c] = 3

    if not cur[r+1, c]:                                         # GRAVITY DROP                 
        nxt[r, c] = 0
        nxt[r+1, c] = 3
    elif not cur[r, c-1] and not cur[r, c+1]:                   # 2 SIDES AVAILABLE
        if not cur[r+1, c-1] and not cur[r+1, c+1]:             # 2 EDGES AVAILABLE
            direction = random.choice([-1, 1])
            nxt[r, c] = 0
            nxt[r, c + direction] = 3
        elif not cur[r+1, c-1]:                                 # CHECK IF LEFT EDGE AVAILABLE
            nxt[r, c] = 0
            nxt[r, c - 1] = 3
        elif not cur[r+1, c+1]:                                 # CHECK IF RIGHT EDGE AVAILABLE
            nxt[r, c] = 0
            nxt[r, c + 1] = 3
        else:
            _random_posible_direction(True, True, r, c, nxt)

    elif not cur[r, c-1]:                                       # ONLY LEFT DIRECTIONS POSSIBLE
        if not cur[r+1, c-1]:                                   # IF ON EDGE THEN GO
            nxt[r, c] = 0
            nxt[r, c - 1] = 3
        else:
            _random_posible_direction(True, False, r, c, nxt)   # Try to randomply move as water do
            
    elif not cur[r, c+1]:                                       # ONLY RIGHT DIRECTIONS POSSIBLE
        if not cur[r+1, c+1]:                                   # IF ON EDGE THEN GO
            nxt[r, c] = 0
            nxt[r, c + 1] = 3
        else:
            _random_posible_direction(False, True, r, c, nxt)   # Try to randomly move as water do
    else:                                                       # WATER IS STACK        
        nxt[r, c] = 3

def sand(nxt, this, r, c, cur):
    if not cur[r+1, c]:                                         # GRAVITY DROP                 
        nxt[r, c] = 0
        nxt[r+1, c] = 4
    elif not cur[r, c-1] and not cur[r, c+1]:                   # 2 SIDES AVAILABLE
        if not cur[r+1, c-1] and not cur[r+1, c+1]:             # 2 EDGES AVAILABLE
            direction = random.choice([-1, 1])
            nxt[r, c] = 0
            nxt[r, c + direction] = 4
        elif not cur[r+1, c-1]:                                 # CHECK IF LEFT EDGE AVAILABLE
            nxt[r, c] = 0
            nxt[r, c - 1] = 4
        elif not cur[r+1, c+1]:                                 # CHECK IF RIGHT EDGE AVAILABLE
            nxt[r, c] = 0
            nxt[r, c + 1] = 4
        else:
            nxt[r, c] = 4

    elif not cur[r, c-1]:                                       # ONLY LEFT DIRECTIONS POSSIBLE
        if not cur[r+1, c-1]:                                   # IF ON EDGE THEN GO
            nxt[r, c] = 0
            nxt[r, c - 1] = 4
        else:
            nxt[r, c] = 4                                       # Try to randomply move as water do
            
    elif not cur[r, c+1]:                                       # ONLY RIGHT DIRECTIONS POSSIBLE
        if not cur[r+1, c+1]:                                   # IF ON EDGE THEN GO
            nxt[r, c] = 0
            nxt[r, c + 1] = 4
        else:
            nxt[r, c] = 4                                       # Try to randomly move as water do
    else:                                                       # WATER IS STACK        
        nxt[r, c] = 4