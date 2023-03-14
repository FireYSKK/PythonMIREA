# // Tiny Sprite Sheet Generator - Frank Force 2020 - MIT License
#
# 'use strict'
# let seed, x, R, i, j, pass, s, X, Y;
#
# seed = Date.now();    // seed for random generaton, can be replaced with hardcoded value
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
from datetime import datetime

seed = int(datetime.timestamp(datetime.now()))
WIDTH = 5
HEIGHT = 5
# x = np.array([[[0] * 3] * WIDTH] * HEIGHT)
x = np.zeros((WIDTH, HEIGHT, 3))


for row in range(HEIGHT):
    for col in range(WIDTH // 2 + 1):
        x[row, col] += np.array([np.random.randint(2)] * 3)

x[:, 3] = x[:, 1]
x[:, 4] = x[:, 0]



# R = lambda s, i: (np.sin(++s + i * i) + 1) * (10 ** 9) % 256 | 0
#
# for i in range(WIDTH * HEIGHT, 0, -1):
#     for p in range(4, 0, 1):
#         s = seed
#         for j in range(R(s, i) / 5 + 50 | 0, 0, -1):
#             X, Y = j&7, j >> 3
#             if R(s, i) < 19:

plt.imshow(x)
plt.show()
