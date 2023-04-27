n = 3000

for i in range (2, n+1):
    x = 0
    for j in range (1, i):
        if i % j == 0:
            x += j
    if x > 1:
        y = 0
        for j in range (1, x):
            if x % j == 0:
                y += j
        
        if i == y and x > i:
            print (i, x)