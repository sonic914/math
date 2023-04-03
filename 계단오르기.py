games = 5
step = 1
pos_a = []
pos_b = []
pos_a.append([2, -1])
pos_b.append([-1, 2])

while step < games: 
    for prev_steps in pos_a:
        temp = []
        for prev_val in prev_steps:
            for j in range(2):
                temp.append(prev_val+2) if j%2 == 0 else temp.append(prev_val-1)
    pos_a.append(temp)
    print ("pos a :", step, pos_a)
    step += 1

step = 1
print

while step < games: 
    for prev_steps in pos_b:
        temp = []
        for prev_val in prev_steps:
            for j in range(2):
                temp.append(prev_val-1) if j%2 == 0 else temp.append(prev_val+2)
    pos_b.append(temp)
    print ("pos b :", step, pos_b)
    step += 1

target_a = pos_a[2]
target_b = pos_b[2]

i=0
while i < len(target_a):
    print ("(",target_a[i],",", target_b[i],")")
    i += 1