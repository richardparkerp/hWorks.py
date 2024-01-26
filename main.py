# Задания №1
# Создайте классы Book и Article, которые реализуют метод word_count.
# Напишите функцию total_words, которая принимает список документов и возвращает общее количество слов.
class Book():
    def __init__(self,cnt):
        self.words=cnt
    def word_count(self):
        return self.words

class Article():
    def __init__(self,cnt):
        self.words=cnt

    def word_count(self):
        return self.words


def total_words(arr):
    total_count=0
    for i in arr:
        total_count+=i.word_count()
    return total_count

book=Book(5)
art=Article(3)
arr=[book,art]

print(total_words(arr))

# Задания №2
# Создайте классы Box и Cylinder, которые реализуют метод volume. Напишите функцию total_volume, которая принимает список контейнеров и возвращает общий объем.

class Box():
    def __init__(self,val1,val2,val3):
        self.side1=val1
        self.side2=val2
        self.side3=val3

    def volume(self):
        return self.side1*self.side3*self.side2


class Cylinder():
    def __init__(self,r,h):
        self.r=r
        self.h=h

    def volume(self):
        return 3.1415*self.h*self.r


arr1=[Box(1,1,1),Box(1,1,1)]
arr2=[Cylinder(1,1)]
arr3=[arr1,arr2]


def total_volume(arr):
    total_volume=0.0
    for i,j in arr:
        for j in arr[i]:
            total_volume+=arr[i,j].volume()

    return total_volume

print(total_volume(arr3))

# Задания №3
# Создайте классы Dog и Cat, которые реализуют метод make_sound. Напишите функцию play_sounds, которая принимает список объектов и вызывает метод make_sound если объект является экземпляром классов Dog или Cat. Используйте функцию isinstance.
