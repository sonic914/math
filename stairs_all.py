import copy

"""
list1 = list2 는 포인터 처럼 동작하므로
list1.copy() 또는 copy.deepcopy()를 사용한다

list1.copy() 는 shallow copy로 부르며
list 내 요소가 객체가 아닌경우 문제 없으나
list 내 요소가 객체인 경우에는
객체의 주소만 복사하여 내부에 포인터로 동작한다

copy.deepcopy()를 사용하면 
모두 값이 복사된다!
"""

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