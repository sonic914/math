import numpy as np
import matplotlib.pyplot as plt

n = 30

A = np.random.randint(0, 1000, (n,1))
min = 1000

for i in range(n):
    if A[i] < min:
        min = A[i][0]
        idx = i
print("Minimum value of A = ", min, 'Index of min(A) = ', idx)

plt.plot(A)
plt.plot(idx, A[idx], 'ro')
plt.show()