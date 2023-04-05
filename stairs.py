winner_steps = 2
loser_steps = -1

player1_pos = 20
player2_pos = -4

turns = player1_pos + player2_pos

max_winner_pos = turns * winner_steps

if player1_pos >= player2_pos:
    winner = "player1"
    winner_pos = player1_pos
else:
    winner = "player2"
    winner_pos = player2_pos

win_turns = turns - (max_winner_pos - winner_pos)/abs(winner_steps - loser_steps)
lose_turns = turns - win_turns

print ("Winner is ", winner)
print ("Turns: %f, wins: %f, lose: %f" % (turns, win_turns, lose_turns))