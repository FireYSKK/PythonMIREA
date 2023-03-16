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
