# 1. Дан список. Определите, является ли он монотонно возрастающим (то есть верно ли, что каждый элемент этого списка больше предыдущего).
# Выведите YES, если список монотонно возрастает и NO в противном случае.
# Решение оформите в виде функции IsAscending(A).
import datetime


def IsAscending(A):
    isAsc=False
    for i in range(len(A)-1):
        if A[i]<A[i+1]:
            isAsc=True
        else:
            return "No"
    return "Yes"

# print(IsAscending([1,2,3,4,1]))

# 2. Дан список чисел, число a и натуральное число k. Выведите индекс k-го по счету появления в массиве числа a.
# Если число a встречается в массиве менее k раз, выведите число -1.

def KthAppearance(A, a, k):
    count=0
    for i,val in enumerate(A):
        if val==a:
           count+=1
        if count==k:
            return i
    return -1

# print(KthAppearance([1,2,3,4,5,5],5,2))

def addToArchive(freSpace,usersCount,valueArr):
    size=freSpace
    valueArr=sorted(valueArr)
    if sum(valueArr)<=freSpace:
        return usersCount
    for i,val in enumerate(valueArr):
        if valueArr[i]<size:
            size-=val
        elif valueArr[i]==val:
            return i
        else:
            return i


# print(addToArchive(400,3,[1000,10000,10000]))

# Напишите программу, в которой необходимо вывести первое слово из строки

def firstWord(str):
    print(str.split()[0])

firstWord("asd , dddd , qwe qwe")


# Напишите программу, которая извлечет дату из строки.

def getDate(str):
    print(datetime.datetime.strptime(str,"%Y-%m-%d"))

getDate("2023-12-01")

# Напишите программу, в которой я ввожу телефонный номер.
# Необходимо проверить правильность формата телефонного номера

import re
def checkNum(str):
    shablon=r'^\+77\d{9}$'
    return bool(re.match(shablon,str))

print(checkNum("+77777777777"))

