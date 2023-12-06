def PrintMap(map):
    for i in range(0,len(map)):
        for i2 in range(0,len(map[i])):
            print(map[i][i2],end=' ')
        if i==2 or i==5 or i==8:
            print()



def endGame(map):
    if map[0][0] and map[1][0] and map[2][0]=='X' or '0':                   # 1 2 3
        return True                                                         # 4 5 6
    elif map[3][0] and map[4][0] and map[5][0]=='X' or '0':                 # 7 8 9
        return True
    elif map[6][0] and map[7][0] and map[8][0]=='X' or '0':
        return True
    elif map[0][0] and map[3][0] and map[6][0]=='X' or '0':
        return True
    elif map[1][0] and map[4][0] and map[7][0]=='X' or '0':
        return True
    elif map[2][0] and map[5][0] and map[8][0]=='X' or '0':
        return True
    elif map[0][0] and map[4][0] and map[8][0]=='X' or '0':
        return True
    elif map[2][0] and map[4][0] and map[6][0]=='X' or '0':
        return True
    else:
        return False


def Game(XorO,map):
    isEnd=False
    isCorrect=False
    while isEnd!=True:
        if(XorO=='X'):
            while isCorrect!=True:
                move=int(input("Enter your move:(num)"))
                if(map[move-1][0]!='X'or'0'):
                    map[move-1][0]='X'
                    isCorrect=True
                    if endGame(map)==True:
                        print("X win!")
                        isEnd=True
            isCorrect=False
            while isCorrect!=True:
                move = int(input("Enter your move:(num)"))
                if (map[move-1][0] != 'X' or '0'):
                    map[move-1][0]='0'
                    if endGame(map) == True:
                        print("0 win!")
                        isEnd = True
                    isCorrect = True
        else:
            while isCorrect != True:
                move = int(input("Enter your move:(num)"))
                if (map[move-1][0] != 'X' or '0'):
                    map[move-1][0] = '0'
                    if endGame(map) == True:
                        print("0 win!")
                        isEnd = True
                    isCorrect = True
            isCorrect = False
            while isCorrect != True:
                move = int(input("Enter your move:(num)"))
                if (map[move-1][0] != 'X' or '0'):
                    map[move-1][0] = 'X'
                    if endGame(map) == True:
                        print("X win!")
                        isEnd = True
                    isCorrect = True



print("X O")
X0=input("Select X or 0:")
s='-'
map=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]
PrintMap(map)
Game(X0,map)





