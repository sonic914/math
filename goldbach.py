import numpy as np

n = 95680

x = np.ones((n, 1))
x[0] = 0

for i in range (2, int(np.sqrt(n))+1):
    for j in range (i+1, n+1):
        if j%i == 0:
            x[j-1] = 0

#x에 1로 남아 있는 배열의 인덱스는 소수임

g = np.array([], dtype=int)

for j in range (n):
    if x[j] == 1:
        g = np.hstack((g, j+1))

#g는 n 까지 소수 리스트

for i in range(len(g)):
    for j in range(i, len(g)):
        if n == g[i] + g[j]:
            print (g[i], g[j])