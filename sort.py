'''
성원정렬 만들어 보기
'''
robot = [1,2,3,4,5,6,7,8,9,10]
power = [23, 5, 83, 6, 10, 31, 13, 19, 9, 20]
temp = []

def pos_sort():
    
    return

position = [[],[],[],[],[],[],[],[],[],[]]

for p in power:
    position[p%10].append(p)

print (position)

for obj in position:
    for t in obj:
        temp.append(t)

print (temp)

position = [[],[],[],[],[],[],[],[],[],[]]

for t in temp:
    position[t//10].append(t)

print (position)

temp = []

for obj in position:
    for t in obj:
        temp.append(t)

print (temp)