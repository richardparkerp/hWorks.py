def PrintMap(map):
    for i in range(0,len(map)):
        for i2 in range(0,len(map[i])):
            print(map[i][i2],end=' ')
        if i==2 or i==5 or i==8:
            print()



def endGame(map):
    if map[0][0]=='X' and map[1][0]=='X' and map[2][0]=='X':                   # 1 2 3
        return True                                                         # 4 5 6
    elif map[3][0]=='X' and map[4][0]=='X' and map[5][0]=='X':                 # 7 8 9
        return True
    elif map[6][0]=='X' and map[7][0]=='X' and map[8][0]=='X':
        return True
    elif map[0][0]=='X' and map[3][0]=='X' and map[6][0]=='X':
        return True
    elif map[1][0]=='X' and map[4][0]=='X' and map[7][0]=='X':
        return True
    elif map[2][0]== 'X' and map[5][0]=='X' and map[8][0]=='X':
        return True
    elif map[0][0]=='X' and map[4][0]=='X' and map[8][0]=='X':
        return True
    elif map[2][0]=='X' and map[4][0]=='X' and map[6][0]=='X':
        return True
    elif map[0][0]=='0' and map[1][0]=='0' and map[2][0]=='0':              # 1 2 3
        return True                                                         # 4 5 6
    elif map[3][0]=='0' and map[4][0]=='0' and map[5][0]=='0':              # 7 8 9
        return True
    elif map[6][0]=='0' and map[7][0]=='0' and map[8][0]=='0':
        return True
    elif map[0][0]=='0' and map[3][0]=='0' and map[6][0]=='0':
        return True
    elif map[1][0]=='0' and map[4][0]=='0' and map[7][0]=='0':
        return True
    elif map[2][0]== '0' and map[5][0]=='0' and map[8][0]=='0':
        return True
    elif map[0][0]=='0' and map[4][0]=='0' and map[8][0]=='0':
        return True
    elif map[2][0]=='0' and map[4][0]=='0' and map[6][0]=='0':
        return True
    else:
        return False


def Game(XorO,map):
    isEnd=False
    isCorrectX=False
    isCorrect0=False
    while isEnd!=True:
        if(XorO=='X'):
            while isCorrectX!=True:
                move=int(input("Enter your move X:(num)"))
                if(map[move-1][0]!='X' and map[move-1][0]!='0'):
                    map[move-1][0]='X'
                    PrintMap(map)
                    isCorrectX=True
                    if endGame(map)==True:
                        print("X win!")
                        isEnd=True
                        isCorrect0=True
                        break
                else:
                    print("Not correct move!Enter again!")
                    isCorrectX=False
            isCorrectX=False
            while isCorrect0!=True:
                move = int(input("Enter your move 0:(num)"))
                if (map[move-1][0] != 'X' and map[move-1][0] !='0'):
                    map[move-1][0]='0'
                    PrintMap(map)
                    isCorrect0=True
                    if endGame(map) == True:
                        print("0 win!")
                        isEnd = True
                        isCorrectX=True
                        break
                else:
                    print("Not correct move!Enter again!")
                    isCorrect0 = False
            isCorrect0 = False
        else:
            while isCorrect0!=True:
                move = int(input("Enter your move 0:(num)"))
                if (map[move-1][0] != 'X' and map[move-1][0] !='0'):
                    map[move-1][0] = '0'
                    PrintMap(map)
                    isCorrect0 = True
                    if endGame(map) == True:
                        print("0 win!")
                        isEnd = True
                        isCorrectX=True
                        break
                else:
                    print("Not correct move!Enter again!")
                    isCorrect0 = False
            isCorrect0 = False
            while isCorrectX != True:
                move = int(input("Enter your move X:(num)"))
                if (map[move-1][0] != 'X' and map[move-1][0] !='0'):
                    map[move-1][0] = 'X'
                    PrintMap(map)
                    isCorrectX=True
                    if endGame(map) == True:
                        print("X win!")
                        isEnd = True
                        isCorrect0=True
                        break
                else:
                    print("Not correct move!Enter again!")
                    isCorrectX = False
            isCorrectX = False



print("X O")
X0=input("Select X or 0:")
s='-'
map=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]
PrintMap(map)
Game(X0,map)
print("End Game!")





