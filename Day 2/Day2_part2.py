import os

os.chdir(os.path.dirname(__file__))

my_score = []
win = 6
draw = 3
lose = 0
rock =1
paper =2
scissors = 3
score_number = 0


with open ('input.txt', 'r') as fle:
    for line in fle:
        opponent = line.strip().split(' ')[0]
        me =line.strip().split(' ')[1]
        if opponent == 'A':
            if me == 'Y':
                my_score.append(draw + rock)
            elif me == 'X':
                my_score.append(lose + scissors)
            else:
                my_score.append(win + paper)
        elif opponent == 'B':
            if me == 'Y':
                my_score.append(draw + paper)
            elif me == 'X':
                my_score.append(lose + rock)
            else:
                my_score.append(win + scissors)
        else:
            if me == 'Y':
                my_score.append(draw + scissors)
            elif me == 'X':
                my_score.append(lose + paper)
            else:
                my_score.append(win + rock)

for score in my_score:
    score_number += score 

print(score_number)

#1 for Rock, 2 for Paper, 3 for Scissors
#Lose you get 0 point, Draw you get 3, Win you get 6 
#A/X = Rock = 1
#B/Y = Paper = 2
#C/Z = Scissors = 3

#Opponent is ABC
#You are XYZ
