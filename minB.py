import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#matplot의 2D 그래프에 3D오브젝트를 그리도록 해주는 라이브러리

nx=10; ny=5
B=np.random.randint(low=1, high=1000, size=(nx, ny))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.linspace(0,nx-1, nx)
y = np.linspace(0, ny-1, ny)
X,Y = np.meshgrid(x,y)
print (X)
print (Y)
print(B)
print (B.T)
ax.plot_wireframe(X,Y,B.T)
s=1000
for i in range(nx):
    for j in range(ny):
        if B[i,j] < s:
            s = B[i,j]
            mini = i
            minj = j
print ('Minimum value of B= ', s)
print ('Index of min(B) with axis row = ', mini)
print ('index of min(B) with axis colum =', minj)
plt.scatter(mini, minj, s, lw=10, c='b')
plt.show()