import matplotlib.pyplot as plt
import numpy as np

WIDTH = 5
HEIGHT = 5
ROWS = 10
COLS = 20
PADDING = 2

sprite_width = WIDTH + PADDING
sprite_height = HEIGHT + PADDING
x = np.zeros((sprite_height * ROWS, sprite_width * COLS, 3))
print(x.shape)

for sprite in range(ROWS * COLS):
    X = sprite // ROWS
    Y = sprite % ROWS
    mid = sprite_width // 2 + sprite_width % 2
    for col in range(1, mid):
        for row in range(1, sprite_height - 1):
            x[Y * sprite_height + row, X * sprite_width + col] += np.array([np.random.randint(2)] * 3)
        x[:, X * sprite_width + (sprite_width - col - 1)] = x[:, X * sprite_width + col]

plt.imshow(x)
plt.show()
