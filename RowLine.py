import numpy as np
import matplotlib.pyplot as plt

nx = 18
ny = 25
for j in range(ny+1):
    plt.plot([0,nx], [j,j], color='k')
plt.axis('image')
plt.show()