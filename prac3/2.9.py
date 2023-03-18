import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time


def dist(a1, a2, b):
    return (a1 - b[0]) ** 2 + (a2 - b[1]) ** 2


img = np.array(Image.open('./src/sanic.jpg'))
WIDTH = img.shape[0]
HEIGHT = img.shape[1]
NODES = 200

leaves = np.random.randint(0, [WIDTH, HEIGHT], size=(200, 2))
start_time = time.perf_counter()

# Simple check, but dist func is adjusted
# Because for comparisone relative distance can be used (instead of absolute)
# A lot of time saved on sqrt calculation

# for row in range(WIDTH):
#     for col in range(HEIGHT):
#         min_dist = (WIDTH + HEIGHT) ** 2
#         closest = [0, 0]
#         for leaf in leaves:
#             d = dist(row, col, leaf)
#             if d < min_dist:
#                 min_dist = d
#                 closest = leaf
#         close_x, close_y = closest
#         img[row, col] = img[close_x, close_y]

# Instead of iterating through all nodes
# Make ndarray with NODES length then substract NODES from it
# That's distances (on x and y axes) from current pixel to each node
# Then normalize and choose the least -> You've got your closest node!

for row in range(WIDTH):
    for col in range(HEIGHT):
        d = np.array([row, col] * NODES).reshape((NODES, 2))
        close_x, close_y = leaves[np.argmin(np.linalg.norm(d - leaves, axis=1))]
        img[row, col] = img[close_x, close_y]


print(time.perf_counter() - start_time)
plt.imshow(img)
plt.show()
