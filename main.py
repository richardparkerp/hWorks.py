def superset(A,B):
    if type(A)!=set:
        print("object 1 is not set")
        return
    elif type(B)!=set:
        print("objet 2 is not set")
        return
    elif type(A)!=set and type(B)!=set:
        print("both objects is not set")
    else:
        if A>B:
            print("first object is superset")
        elif B>A:
            print("second object is superset")
        else:
            print("objects are equal")

#
# Aa={1,2,3}
# Bb={1}
# superset(Bb,Aa)


#2
# Создайте программу «Англо-французский словарь». Нужно хранить слово на
# английском языке и его перевод на французский. Требуется реализовать возможность
# добавления, удаления, поиска, замены данных. Используйте словарь для хранения
# информации.

# dict={"word":"slovo","bird":"ptica","dictianory":"slovar"}
# arr=[]
# choise=-1
# while choise!=0:
#     print("1 - add "
#           "2 - remove"
#           "3 - search"
#           "4 - replace")
#     choise=int(input("Enter your choise:"))
#     if choise==1:
#         new_word=input("Enter two words: (word translate)")
#         arr=new_word.split(' ')
#         dict.update({arr[0]:arr[1]})
#         print(dict)
#     elif choise==2:
#         remove=input("Enter word for delete:")
#         dict.pop(remove)
#         print(dict)
#     elif choise==3:
#         search=input("Enter word for search:")
#         dict.get(search)
#         print(dict)
#     elif choise==4:
#         replace=input("Enter two words: (word and new value)")
#         arr=replace.split(' ')
#         dict[arr[0]]=arr[1]
#         print(dict)
#     elif choise==0:
#         print("GoodBye!")
#     else:
#         print("choise is not correct!")

#  Предоставлен список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу: например, если
# число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка
# «44» (второе повторение, т.е. число дублируется в строке), строка «444» (третье повторение,
# т.е. строка множится на 3).
# Реализуйте вывод множества через функцию set_gen().


asd=[1,2,2,2,3,4,5,6,7,8,9,9,10]

# def set_gen(arr):
#     i=0
#     answ=set()
#     for i in arr:
#         count = arr.count(i)
#         if count>1:
#             answ.add(str(i)*count)
#         else:
#             answ.add(i)
#     print(answ)
#
# set_gen(asd)


# 1. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию
# biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ:
# значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента
# «first_one» со значением «we can do it». Воссоздайте эту функцию


my_dict={"first_one":"we can do it"}

print(type(my_dict)

