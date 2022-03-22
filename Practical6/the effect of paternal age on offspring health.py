"""
=============
scatter(x, y)
=============

See `~matplotlib.axes.Axes.scatter`.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
x = (30,35,40,45,50,55,60,65,70,75)
y = (1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94)

plt.scatter(x,y)

plt.show()
