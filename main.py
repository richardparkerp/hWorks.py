# Напишите программу, где я ввожу логин и пароль. И если данные были введены верно,
# то мы выводим Authentication completed, иначе Invalid login or password. Правильность логина не зависит от
# (Логин должен быть user, пароль - qwerty)
login = input("Enter login : ")
password = input("Enter password : ")

if (login == "user" and password == "qwerty"):
    print("Authentication completed!")
else:
    print("Invalid login or password!")

# Напишите программу обмена валют, где я ввожу сумму в тенге
# и выбираю на какую валюту хочу перевести. (Курс USD – 420, EUR – 510, RUB - 5.8).

sum=-1
while(sum<=0):
    sum = int(input("Enter your sum im KZT: "))
    print("CHOISE CONVERT VALUTE\n"
          "1 - USD\n"
          "2 - EUR\n"
          "3 - RUB\n"
          "0 - Exit")
    choise=input("YOUR CHOISE : ")
    if choise=="1":
        answer = sum/420
        print("Anwer %.2f" % answer + "USD")
    elif choise=="2":
        answer = sum / 510
        print("Anwer %.2f" % answer + "EUR")
    elif choise=="3":
        answer = sum / 5.6
        print("Anwer %.2f" % answer + "RUB")
    elif choise==0:
        print("bye bye!")
    else:
        print("Please , enter again!")



def checkCash(s,p,m):
    if s+p>m:
        print("No")
    else:
        print("Yes")

checkCash(120,100,220)

def checkLucky(str):
    n1 = int(str[0])+int(str[1])+int(str[2])
    n2 = int(str[len(str)-1])+int(str[len(str)-2])+int(str[len(str)-3])
    if n1 == n2 :
        print("Lucky")
    else:
        print("Simple!")

checkLucky("123123")

n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)


num=int(input("Enter num :"))
s=""
for i in range(1 ,num+1):
    s+=str(i)
    print(s)


n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)


num=int(input("Etner num :"))

for i in range(1,num+1):
    if i**2<=num:
        print(i**2,end=" ")
    else:
        break