import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def dist(a1, a2, b):
    return ((a1 - b[0]) ** 2 + (a2 - b[1]) ** 2) ** 0.5


img = np.array(Image.open('./src/sanic.jpg'))
WIDTH = img.shape[0]
HEIGHT = img.shape[1]

leaves = np.random.randint(0, [WIDTH, HEIGHT], size=(200, 2))

for row in range(WIDTH):
    for col in range(HEIGHT):
        min_dist = (WIDTH + HEIGHT) * 2
        closest = [0, 0]
        for leaf in leaves:
            d = dist(row, col, leaf)
            if d < min_dist:
                min_dist = d
                closest = leaf
        close_x, close_y = closest
        img[row, col] = img[close_x, close_y]
    print(row)


plt.imshow(img)
plt.show()
