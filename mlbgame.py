#Simulador de jogo da MLB

#Programar placar
import random
#starting score
rs_score = [0,0,0,0,0,0,0,0,0]
y_score = [0,0,0,0,0,0,0,0,0]
rs_tscore = sum(rs_score)
y_tscore = sum(y_score)

print(f'        1 2 3 4 5 6 7 8 9 R')
print(f'REDSOX  {rs_score[0]} {rs_score[1]} {rs_score[2]} {rs_score[3]} {rs_score[4]} {rs_score[5]} {rs_score[6]} {rs_score[7]} {rs_score[8]} {rs_tscore}')
print(f'YANKEES {y_score[0]} {y_score[1]} {y_score[2]} {y_score[3]} {y_score[4]} {y_score[5]} {y_score[6]} {y_score[7]} {y_score[8]} {y_tscore}')


for num in range(8):
    rs_score[num] = random.randint(0,4)
    y_score[num] = random.randint(0,3)
    
#total score
rs_tscore = sum(rs_score)
y_tscore = sum(y_score)

#New Score
print(f'        1 2 3 4 5 6 7 8 9 R')
print(f'REDSOX  {rs_score[0]} {rs_score[1]} {rs_score[2]} {rs_score[3]} {rs_score[4]} {rs_score[5]} {rs_score[6]} {rs_score[7]} {rs_score[8]} {rs_tscore}')
print(f'YANKEES {y_score[0]} {y_score[1]} {y_score[2]} {y_score[3]} {y_score[4]}