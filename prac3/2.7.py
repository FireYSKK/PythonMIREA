import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open('./src/sanic.jpg'))
print(repr(img))

plt.imshow(img)
plt.show()
