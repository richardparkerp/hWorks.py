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

def biggest_dict(**kwargs):
    for name,value in kwargs.items():
        my_dict[name]=value

def pucking_dict(**kwargs):
    return kwargs
def unpucking(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
# print(my_dict)

biggest_dict(world="asdsd",asda="asdasd")

# print(my_dict)



# 2. Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый
# и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key» со
# значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался
# тем же (имел тот же адрес в памяти).

# dict={"1":"one","2":"two","3":"three","4":"four"}
#
# print(dict)
# first_key,last_key=list(dict.keys())[0],list(dict.keys())[-1]
# dict[first_key],dict[last_key]=dict[last_key],dict[first_key]
# dict={last_key if k==first_key else first_key if k==last_key else k:v for k, v in dict.items()}
# print(dict)
# second_key=list(dict.keys())[1]
# del dict[second_key]
# print(dict)
# dict["new_key"]="new value"
# print(dict)


#  Есть некоторый словарь, который хранит названия стран и столиц. Название страны
# используется в качестве ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск данных, редактирование данных,
# сохранение и загрузку данных (используя упаковку и распаковку).

my_dict={"Kazakhstan":"Astana","Russia":"Moscow","Canada":"Ottawa"}

choise='-1'

while choise!="0":
    print("1 - Add new element\n2 - Remove element\n3 - Search element\n4 - Edit element\n5 - Save\n6 - Update dictianory")
    choise=input("Enter ur choise:")
    if choise=="1":
        new_key=input("Enter country name:")
        new_value=input("Enter capital city name:")
        my_dict[new_key]=new_value
        print("New element added")
        print("----------------------------------------------------")
    elif choise=="2":
        key_del=input("Enter country name to be deleted:")
        del my_dict[key_del]
        print("Element removed!")
        print("----------------------------------------------------")
    elif choise=="3":
        search_element=input("Enter the name search element:")
        if search_element in my_dict:
            print(my_dict[search_element])
        else:
            print("This element does not exist ")
    elif choise=="4":
        edit_key=input("Enter edit country name:")
        if edit_key in my_dict:
            edit_value=input("Enter new value:")
            my_dict[edit_key]=edit_value
        else:
            print("This element does not exist ")
    elif choise=="5":
        print(my_dict)
    elif choise=="6":
        inp=input("1 - pucking\n2 - unpucking:")

        if inp=="1":
            my_dict.update(pucking_dict(USA="Washington"))
            print(my_dict)
        elif inp=="2":
            unpucking(**my_dict)
        else:
            print("Error")
    else:
        print("Error")





