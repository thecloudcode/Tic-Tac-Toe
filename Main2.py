import numpy as np

def board_print(a):
    for i in range(2):
        print(' | '.join(a[i]))
        print('---------')
    print(' | '.join(a[2]))
    # for i in range(3):
    #     for j in range(3):
    #         print('X' if a[i][j]=='1' else 'O' if a[i][j]=='2' else '-',end=" ")
    #         if j<2:
    #             print('|',end=" ")
    #         else:
    #             print()
    #     if i < 2:
    #         print('---------')

def win_check(a):
    for i in a:
        if np.count_nonzero(i == 'X')==3:
            return 1
        elif np.count_nonzero(i == 'O')==3:
            return 2
    index=0
    col=[]
    for i in range(3):
        for j in a:
            col.append(j[index])
        if col.count('X')==3:
            return 1
        elif col.count('O')==3:
            return 2
        col=[]
        index+=1
    if a[1][1]=='X' or a[1][1]=='O':
        if a[0][0]==a[1][1]==a[2][2]=='X':
            return 1
        if a[0][2]==a[1][1]==a[2][0]=='O':
            return 2

    for i in a:
        for j in i:
            if j!='O' and j!='X':
                return 0
    return 3

def choice_maker(choice,a,player):
    if choice==1:
        a[2][0]='X' if player==1 else 'O'
    if choice==2:
        a[2][1]='X' if player==1 else 'O'
    if choice==3:
        a[2][2]='X' if player==1 else 'O'
    if choice==4:
        a[1][0]='X' if player==1 else 'O'
    if choice==5:
        a[1][1]='X' if player==1 else 'O'
    if choice==6:
        a[1][2]='X' if player==1 else 'O'
    if choice==7:
        a[0][0]='X' if player==1 else 'O'
    if choice==8:
        a[0][1]='X' if player==1 else 'O'
    if choice==9:
        a[0][2]='X' if player==1 else 'O'

score1=0
score2=0
class AlreadyExists(Exception):
    pass
class OutOfChoice(Exception):
    pass


board = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']])
alreadychosen=[]

if(input("Type 'Start' to start the game\n").lower()=='start'):
    print()
    player1 = input("Player 1 Name: ")
    player2 = input("Player 2 Name: ")
    while(1):
        board_print(board)

        print("\nPlayer 1 Starts...\nKeep your choice from 1 to 9\n")
        player=1

        while(1):
            try:
                choice=int(input())
                if choice<1 or choice>9:
                    raise OutOfChoice
                if choice in alreadychosen:
                    raise AlreadyExists
                else:
                    alreadychosen.append(choice)
            except ValueError:
                print("Given Input is not a number!")
                continue
            except AlreadyExists:
                print("The given cell is already filled!")
                continue
            except OutOfChoice:
                print("Please enter a number between 1 and 9!")
                continue

            choice_maker(choice,board,player)
            board_print(board)
            player=2 if player==1 else 1

            winner=win_check(board)
            if winner != 0:
                if winner==3:
                    print("\nDraw\n")
                elif winner==1:
                    print(f"\n{player1} Wins!")
                    score1+=1
                else:
                    print(f"\n{player2} Wins!")
                    score2+=1
                print(f"Score : {score1}:{score2}")
                break

        re=input("\nEnter 'Restart' to restart:\n").lower()
        if re=='restart':
            board = np.array([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']])
            alreadychosen=[]
        else:
            break

else:
    print('End')