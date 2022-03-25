import matplotlib.pyplot as plt
import numpy as np

a = (45,36,86,57,53,92,65,45)# the data
fig, ax = plt.subplots()
VP = ax.boxplot(a)# the graph model is a boxplot
plt.show()# show the boxplot