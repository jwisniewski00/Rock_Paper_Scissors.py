from random import randint
print('This is a rock paper scissors game')
c_win = 0
u_win = 0
while True:
    x = input('Type "r" for Rock or "p" for Paper or "s" for Scissors. If you want to end the game type random key: ')
    if x not in ["r", "p", "s"]:
        break
    computer = randint(1, 3)
    choices = {'r': 1, 'p': 2, 's': 3}
    user = choices[x]
    num_fig = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    print('\n')
    if user == computer:
        print(f" {num_fig[user]}  vs {num_fig[computer]}  IT'S A DRAW!      You : {u_win} , Computer : {c_win}")
    elif user == 1 and computer == 2 or user == 2 and computer == 3 or user == 3 and computer == 1:
        c_win += 1
        print(f" {num_fig[user]}  vs {num_fig[computer]}  YOU LOSE!         You : {u_win} , Computer : {c_win}")
    else:
        u_win += 1
        print(f" {num_fig[user]}  vs {num_fig[computer]}  YOU WIN!          You : {u_win} , Computer : {c_win}")
    print('\n')