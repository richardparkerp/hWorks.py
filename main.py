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
        print(f"{sum/420}USD")
    elif choise=="2":
        print(f"{sum/510}EUR")
    elif choise=="3":
        print(f"{sum/5.8}RUB")
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