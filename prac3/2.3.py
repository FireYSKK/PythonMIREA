# // Tiny Sprite Sheet Generator - Frank Force 2020 - MIT License
#
# 'use strict'
# let seed, x, R, i, j, pass, s, X, Y;
#
# seed = Date.now();    // seed for random generation, can be replaced with hardcoded value
# x = c.getContext`2d`; // 2d canvas context
# x.lineWidth = 2;      // set 2 pixel wide line width to make the black outline
# R = ()=> (Math.sin(++s + i*i) + 1)*1e9 % 256 | 0; // get a seeded random integer between 0-256
#
# for(i = 32 * 16; i--;)                          // for each sprite (32 rows x 16 columns)
# for(pass = 4; pass--;)                          // 4 passes, outline left/right and fill left/right
# for(s = seed, j = R()/5 + 50|0; j--;)           // set seed, randomize max sprite pixels, 50-101
#   X = j&7, Y = j>>3,                            // X & Y pixel index in sprite
#   R() < 19 ?                                    // small chance of new color
#     x.fillStyle = `rgb(${R()},${R()},${R()})` : // randomize color
#     R()**2 / 2e3 > X*X + (Y-5)**2 &&            // distance from center vs random number
#       x[pass&2 ? 'strokeRect' : 'fillRect'](    // stroke first for outline then fill with color
#           7 + i%32*16 - pass%2*2*X + X,         // x pos, flipped if pass is even
#           2 + (i>>5)*16 + Y,                    // y pos
#           1, 1);                                // 1 pixel size


import matplotlib.pyplot as plt
import numpy as np


def R():
    return np.random.random()


WIDTH = 7
HEIGHT = 7
ROWS = 10
COLS = 20
PADDING = 4
ONE_SIDE_PADDING = PADDING // 2
COLOR_SWITCH_PROB = 33 / 256

sprite_width = WIDTH + PADDING
sprite_height = HEIGHT + PADDING
x = np.zeros((sprite_height * ROWS, sprite_width * COLS, 3))

for sprite in range(ROWS * COLS):
    X = sprite // ROWS
    Y = sprite % ROWS
    mid = sprite_width // 2 + sprite_width % 2
    # 2 passes: for outline and for color filling
    for step in range(2):
        color = np.array([R(), R(), R()])
        # Going through sprite
        for col in range(ONE_SIDE_PADDING, mid):
            for row in range(ONE_SIDE_PADDING, sprite_height - ONE_SIDE_PADDING):
                if step == 0:
                    x[Y * sprite_height + row, X * sprite_width + col] += [np.random.randint(2) * 255] * 3
                else:
                    x[Y * sprite_height + row, X * sprite_width + col] *= color / 255
                    if R() < COLOR_SWITCH_PROB:
                        color = np.array([R(), R(), R()])
            x[:, X * sprite_width + (sprite_width - col - 1)] = x[:, X * sprite_width + col]

plt.imshow(x)
plt.show()
