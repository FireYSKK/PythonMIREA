import matplotlib.pyplot as plt
import numpy as np

WIDTH = 5
HEIGHT = 5
x = np.zeros((WIDTH, HEIGHT, 3))


for row in range(HEIGHT):
    for col in range(WIDTH // 2 + 1):
        x[row, col] += np.array([np.random.randint(2)] * 3)

x[:, 3] = x[:, 1]
x[:, 4] = x[:, 0]


plt.imshow(x)
plt.show()
