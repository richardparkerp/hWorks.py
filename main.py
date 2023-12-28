# Задание №1.
# Напишите программу для создания списка, длина которого равна N. После создания списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных, вывод должен быть «Нет», в остальных ключах «Да».
# Input
# 5
# 4 16 19 31 2
# Output
# 19 31
# 4 16 2
# YES
import random
def createList(N):
    list=[random.randint(1,99) for _ in range(N)]
    print(list)
    cnt1=[x for x in list if x%2==0]
    print(cnt1)
    cnt2=[x for x in list if x%2!=0]
    print(cnt2)
    if len(cnt1) > len(cnt2):
        print("YES")
    elif len(cnt2) > len(cnt1):
        print("NO")
    else:
        print("EQUAL")


# createList(10)


# Задание №2.
# Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму элементов главной диагонали.
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Diagonals : 1 + 5 + 9 = 15

def matrixFunc():
    list=[[random.randint(1,10) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            print(list[i][j] , end=" ")
        print()
    sum=list[0][0]+list[1][1]+list[2][2]
    print(sum)

matrixFunc()

# Задание №3.
# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……

def n_fibonachi(n):
    if n<1:
        return 1
    else:
        return n_fibonachi(n-1)+n_fibonachi(n-2)

fib_val=4
# print(n_fibonachi(fib_val))

# Задание №4.
# Напишите функцию, которая проверяет является ли число степенью двойки. Если истинно выведите True, иначе False.
# Input
#  8
# Output
#  True
def two_digit(n):
    if n%2==0:
        return True
    else:
        return False

# print(two_digit(12))


# Задание №5
# Реализовать инженерный калькулятор, для всех арифметических действий, включая нахождение факториала, Фибоначчи, и всех тригонометрических функций, также возведения числа в степени.
# В ходе решения, допустимо использования модуля math, функции определяемой пользователем, рекурсивной функции и лямбда-функции.
# Реализуйте диалог с пользователем.
import math
# isEnd=False
# while isEnd!=True:
#     print("1 - Нахождение Фибоначи \n2 - Тригонаметрчиские фцнкий \n3 - Возведенгие числа в степень \n  ")
#     choise = input("Выберите опреацию - ")
#     if choise =="1":
#         fib=int(input("Введите число : (не меньше 1)"))
#         if fib>1:
#             print(n_fibonachi(fib))
#         else:
#             print("Введите снова!")
#     elif choise =="2":
#         num=int(input("Введите ваше число - "))
#         print("1 - синус \n2 - косинус")
#         temp=input("Ваш выбор - ")
#         if temp=="1":
#             print(math.sin(num))
#         elif temp=="2":
#             print(math.cos(num))
#         else:
#             print("Ошибка выбора!")
#     elif choise=="3":
#         num=int(input("Введите возведимое число:"))
#         isTrue=False
#         while isTrue!=True:
#             s=int(input("Введите степень в котрое нужно возвести: (больше нуля)"))
#             if s>0:
#                 print(f"answer is {num**s}")
#                 isTrue=True
#     elif choise=="0":
#         isEnd=True
#     else :
#         print("Неверная команда! Введите снова!")


# Модули и пакеты
# Задание №1. Спроектировать программу для определения победителя на выборах.
# Пользователю предоставляется список кандидатов, каждый из голосующих делает свой выбор.
# Выбранный кандидат добавляется в список. В итоге имеется неизменяемый список кандидатов.
# Определить победителя, в зависимости от количества встречаемости в списке кандидата.
# Определить количество голосов победителя.
# В случае, если будет двое победителей, сделать сортировку по длине слова между ними и выбрать победителя с минимальным количеством букв в имени.

condidats=["Elcin","Putin","Nazarbaev","Stalin","Mavrodi"]
# print(' '.join(condidats))
votes=[]
for id,val in enumerate(condidats):
    print(f"{id+1} - {val}")

for i in range(10):
    isTrue=False
    while isTrue!=True:
        vote=int(input(f"User number {i+1} Indicate your vote: "))
        if vote<=len(condidats):
            votes.append(condidats[vote-1])
            isTrue=True
        else:
            print("Wrong choice!Indicate your vote again!")

votes_count={}
for i in range(5):
    votes_count[condidats[i]]=votes.count(condidats[i])


max_value=0
for i in votes_count:
    if votes_count[i]>max_value:
        max_value=votes_count[i]

winners=[]
for i in votes_count:
    if votes_count[i]==max_value:
        winners.append(i)
winner=""
for i in winners:
    if len(winner)<len(i):
        winner=i

print(f"Winner is {winner}")



