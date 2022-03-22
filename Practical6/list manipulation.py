import matplotlib.pyplot as plt
import numpy as np

a = (45,36,86,57,53,92,65,45)
fig, ax = plt.subplots()
VP = ax.boxplot(a)
plt.show()