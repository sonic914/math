import numpy as np

def find_prime (n):
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
    return g

def goldbach_2 (prime_list):
    count = 0
    for i in range(len(prime_list)):
        for j in range(i, len(prime_list)):
            for k in range (j, len(prime_list)):
                if n == prime_list[i] + prime_list[j] + prime_list[k]:
                    count += 1
                    print (count, ":", prime_list[i], prime_list[j], prime_list[k])

end = 1000
for n in range (6, end+1):
    print (n, "에 대한 검색")
    primes = find_prime(n)
    goldbach_2(primes)
