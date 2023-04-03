import numpy as np
import matplotlib.pyplot as plt

nx = 18
ny = 25
for i in range(nx+1):
    plt.plot([i,i], [0,ny], color="k")
plt.axis('image')
plt.show()