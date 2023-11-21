#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 500)
X, Y = np.meshgrid(x, x)

radius = 0.5
disc = (X ** 2) + (Y ** 2) < radius ** 2
plt.imshow(disc, cmap="gray")
plt.show()
