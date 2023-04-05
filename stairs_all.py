import copy

turns = 5

pre_result = []
cur_result = []

games = 0

if turns == 0:
    exit()

for i in range(2):
    if i%2 == 0:
        cur_result.append(['win'])
    else:
        cur_result.append(['lose'])

pre_result = copy.deepcopy(cur_result)
cur_result = []

while games+1 < turns:
    for i in pre_result:
        for j in range(2):
            tmp = copy.deepcopy(i)
            if j%2 == 0:
                tmp.append("win")
            else:
                tmp.append('lose')
            cur_result.append(tmp)
    #print (cur_result, "\n")
    pre_result = copy.deepcopy(cur_result)
    cur_result = []
    games += 1

player1_pos = []
player2_pos = []

for i in pre_result:
    position1 = 0
    position2 = 0
    for j in i:
        if j == 'win':
            position1 += 2
            position2 += -1
        else:
            position1 += -1
            position2 += 2
    player1_pos.append(position1)
    player2_pos.append(position2)

for i in range(len(player1_pos)):
    print ("(", player1_pos[i], ", ", player2_pos[i],")")