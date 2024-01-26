# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

class Car():
    def __init__(self):
        self.modelName=""
        self.year_of_issue=1900
        self.manufacturer=""
        self.engine_capacity=0.0
        self.color=""
        self.price=0.0

    def isnertInfo(self):
        info=""
        isCorrect=False
        while isCorrect!=True:
            info=input("Enter model name: ")
            if info:
                self.modelName=info
                isCorrect=True
        isCorrect=False
        while isCorrect!=True:
            info=int(input("Year of issue: "))
            if info:
                self.year_of_issue=info
                isCorrect=True

        isCorrect=False
        while isCorrect!=True:
            info=input("Enter manufacturer: ")
            if info:
                self.manufacturer=info
                isCorrect=True
        isCorrect=False
        while isCorrect!=True:
            info=float(input("Enter engine capacity: "))
            if info:
                self.engine_capacity=info
                isCorrect=True
        isCorrect=False
        while isCorrect!=True:
            info=input("Enter color of car: ")
            if info:
                self.color=info
                isCorrect=True
        isCorrect=False
        while isCorrect!=True:
            info=float(input("Enter the price of the car: "))
            if info:
                self.price=info
                isCorrect=True

        print("Well done. Information saved!")

    def printInfo(self):
        print(f"Model name : {self.modelName}")
        print(f"Year of issue : {self.year_of_issue}")
        print(f"Manufacture : {self.manufacturer}")
        print(f"Color : {self.color}")
        print(f"Price : {self.price}")

    def set_name(self,new_name):
        if type(new_name)==str:
            self.modelName=new_name
    def get_name(self):
        return self.modelName

    def set_color(self,new_color):
        if type(new_color)==str:
            self.color=new_color

    def get_color(self):
        return self.color



car=Car()
car.isnertInfo()
car.printInfo()



# Реализуйте класс «Книга».
# Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через
# модификаторы доступа и свойства



class Book():
    def __init__(self):
        self.name=""
        self.year_of_issue=None
        self.publisher=""
        self.jenre=""
        self.author=""
        self.price=None

    def initBook(self):
        # было поздно и к сожалению е было не было времени на проверку введенных данных
        self.name=input("Enter book name: ")
        self.year_of_issue=input("Enter year of issue: ")
        self.publisher=input("Enter publisher name: ")
        self.jenre=input("Enter jenre type: ")
        self.author=input("Enter author name: ")
        self.price=input("Enter the price: ")

    def printInfo(self):
        print(f"Book name: {self.name}")
        print(f"Year of issue: {self.year_of_issue}")
        print(f"Publisher name: {self.publisher}")
        print(f"Jenre name: {self.jenre}")
        print(f"Author name: {self.author}")
        print(f"Price: {self.price}")


    @property
    def _name(self):
        return self.name

    @_name.setter
    def _name(self):
        self.name=input("Enter name: ")

    @property
    def _author(self):
        return self.name

    @_author.setter
    def _author(self):
        self.author=input("Enter author name: ")



book=Book()
book.printInfo()
