import numpy as np
import matplotlib.pyplot as plt

nx = 18
ny = 25

for j in range(ny+1):
    plt.plot([0,nx], [j,j], "k--")
for i in range(nx+1):
    plt.plot([i,i], [0,ny], "k--")

numOfHome = 30
x = np.random.randint(low=0, high=nx+1, size=(numOfHome, 1))
y = np.random.randint(low=0, high=ny+1, size=(numOfHome, 1))
plt.plot(x, y, 'bo')
firestationX = 4
firestationY = 11
plt.plot(firestationX, firestationY, 'rs')
plt.axis("image")
plt.show()

sumOfDistances = 0
for k in range(numOfHome):
    sumOfDistances += abs(x[k]-firestationX)+abs(y[k]-firestationY)
print ("Sum of distances :", sumOfDistances)
