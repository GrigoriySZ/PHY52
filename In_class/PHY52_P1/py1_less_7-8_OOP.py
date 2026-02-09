# Объектно ориентированное программирование (ООП)

'''
3 кита ООП:
1. Инкапсуляция - это объединение данных и методов работы с ними.
1.1. Переменные внутри класса называют полями класса
1.2. Функции внутри класса называют методами класса
1.3. Сокрытие - все полня должны быть недоступны для измненения извне 

2. Наследование (обобщение) - потомок наследует (расширяет) поля и методы родителя
extend - расширяе

3. Полиморфизм - любой класс может использоваться в контексте самого себя, 
так и в контексте его родителей

4. Абстракция (слабо реализована в Python)

Инкапслулированный объект называется классом (class)
Класс по сути является пользовательским типом данных
Параметр self, передаваемый в методы, хранит ссылку на объект
для которого метод вызван.

__init__ - инициализатор или функция(метод)-конструктор.
Она вызывается при создании объектов, принимает стартовые значения для полей

Методы с описаные __method__ с двух сторон называю магическими методами (magic method)

Методы, которые меняют поля класса (по заданным условиям), называются set-методы или сеттеры
Методы, которые передают данные при помощи оператора return, называются get-методы или геттеры

Поля, названия которых, начинаются с _ считаются скрытыми
Метод с __ в начале является приватным и к нему обращаеся только внутри класса
Взаимодействовать с полем можно в рамках языка, но категорически запрещено

Главное отличие свойства @property от поля в том, что свойства реалзуюе логику 
прописанных геттеров и сеттеров

@ - знак декоратора

Ассоциация - класс хранит ссылку на другой класс, из которого он перенимает параметры

SOLID - ряд принципов для проектирования классов: 

S - Single responsibility prc. - принцип единственной ответственности 
    (один класс - одна задача)
O - Open/Close prc. - принцип открытости/закрытости 
    (Классы должны быть открыты для расширения, но закрыты для изменения)
L - Liskov's substitution prc. (LSP) - принцип подстановки Лисков 
    (Функция должна работать с подтипами базового типа не знаю об этом)
I - Interface segregation prc. (ISP) - Принципе разделения интерфейсов
    (Много специализированных интерфейсов лучше, чем один общего назначения)
D - Dependency inversion prc. (DIP) - уровень абстракции не может оставться постоянным, 
    он может либо повышаться, либо уменьшаться

'''

# ИНКАПСУЛЯЦИЯ

class Player:
    
    def __init__(self, health: int = 10):
        self.max_hp = 30
        if health > self.max_hp: 
            self.hp = self.max_hp
        else:
            self.hp = health
        
    def takeDamage(self, damage: int):
        if damage < 0:
            damage = 0
        if self.hp <= damage:
            self.hp = 0
        else:
            self.hp -= damage

    def takeHeal(self, heal: int):
        if self.hp + heal > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heal


# vasia = Player(10)
# print(vasia.hp)
# vasia.takeDamage(5)
# print(vasia.hp)
# vasia.takeDamage(3)
# print(vasia.hp)
# petia = Player(25)
# petia.takeDamage(5)
# print(petia.hp)
# vasia.takeHeal(40)
# print(vasia.hp)
# vasia.takeDamage(-100)
# print(vasia.hp)

class User:

    def __init__(self, name: str, age: int, balance: int):
        
        if name != "":
            self.__name = name
        else:
            name = "не указано"
        
        if age < 18:
            self.__age = 18
        else:
            self.__age = age

        if balance < 0:
            self.__balance = 0
        else:
            self.__balance = balance

    def set_name(self, new_name: str):
        if new_name != "":
            self.__name = new_name
        
    def get_name(self):
        return self.__name.capitalize()

    # Создание свойства через декоратор (@) property
    # Свойства принято называть с большой буквы 
    @property
    def Balance(self):
        return self.__balance
    # Добавить к свойству Balance setter
    @Balance.setter
    def Balance(self, newBalance: int):
        if newBalance >= 0:
            self.__balance = newBalance

    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self, newAge: int):
        if newAge > 18:
            self.__age = newAge
    
    # Метод снять со счета
    def take_money(self, money: int):
        if self.__balance - money >= 0 and money > 0:
            self.__balance -= money

    # Метой внести на счет
    def put_monet(self, money: int):
        if money > 0:
            self.__balance += money


arcadi = User("Аркадий", 27, 3000)

arcadi.set_name("Акакий")
print(arcadi.get_name())

# Неправильный способ обращения и изменения полей объекта
# arcadi.__name = "Акакий"
# print(arcadi.__name)

print(arcadi.Balance)
arcadi.Balance = -1000
print(arcadi.Balance)

class Department:
    def __init__(self, name: str):
        self.__name = name

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, new_name: str):
        self.__name = new_name

class Employer:
    def __init__(self, fio: str, age: int, salary: int, depart: Department):
        self.__fio = fio
        self.__age = age
        self.__salary = salary
        self.__depart = depart
    
    # Статический метод для альтернативного аврианты задачи 
    def get_instance(f_name: str, m_name: str, l_name:str,
                 age: int, salary: int, depart: Department):
        return Employer(f_name+m_name+l_name, age, salary, depart)
    
    # Магический метод строкового представления объектов
    def __str__(self):
        return f"ФИО: {self.__fio}, Возраст: {self.__age}, Зарплата: {self.__salary}, Отдел: {self.__depart.Name}"
    
    @property
    def Department(self):
        return self.__depart
    
    @Department.setter
    def Department(self, new_depart: Department):
        self.__depart = new_depart

    def __add__(self, other):
        if isinstance(other, Employer):
            res = Employer(self.__fio, (self.__age + other.__age) // 2,
                            self.__salary + other.__salary, other.__depart)
            return res
    
    # Магический метод __hash__ перегружается для определения логики распределения объекта 
    # в хэш таблицах  
    def __hash__(self):
        pass


d1 = Department("Разработка")
e1 = Employer("Иванов Иван Иванович", 30, 60_000, d1)
e2 = Employer("", 35, 50_000, d1)
# print(e1 + e2)
# e1.__str__()
print(e1)
print(e1.Department.Name)
# Вызов статического метода
e3 = Employer.get_instance("A", "B", "C", 32, 30_900, d1)
print(e3)
d1.Name = "Тестирование"
print(e1.Department.Name)

# НАСЛЕДОВАНИЕ

class Point2d:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

# Супер-класс super() - класс родителя, от которого будут наследованы методы, поля и логика работы с ними

class Point3d(Point2d):
    def __init__(self, x: int, y: int, z: int):
        super().__init__(x, y)
        self.__z = z

    def function(self, x):
        self.__x = x

# Метод по умолчанию может задан в классе-родителе и по умполчанию идет у потомков, 
# но может быть перезаписан у потомков, если необходимо

# Класс Animal является абстрактным. 
# Этот класс является абстрактны из-за того, он выражен без достаточной конркетики.
# На основе абстрактного класса невозможно создать объект, т.к. у него не до конца реализована логика

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав-гав")

class Cat(Animal):
    def make_sound(self):
        print("мяу")

def functiom(a: Animal):
    a.make_sound()

c = Cat()
functiom(c)
c.make_sound()

# Параллельное (асинхронное) программирование 

# Аpplication public interface (API) - публичный интерфейс приложения
