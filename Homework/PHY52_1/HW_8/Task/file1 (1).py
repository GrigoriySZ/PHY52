#инкапсуляция
#наследование
#полиморфизм
#абстракция

#инкапсуляция это объединение данных и методов работы с ними
#переменные внутри класса называют полями класса
#функции внутри класса - методами класса
#параметр self, передаваемый в методы, хранит ссылку на
#объект для которого метод вызван
#__init__ - функция-конструктор, она вызывается при создании
#объекта, принимает стартовые значения для полей
#сокрытие - все поля должны быть не доступны для изменения
#из вне
#методы, которые меняют поля класса (по заданным условиям)
#называются set-методы или сеттеры
#поля, названия которых, начинаются с _ считаются скрытыми
class Player:
    def __init__(self, health: int):
        self.max_hp = 30
        if health > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = health
    def takeDamage(self, damage: int):
        if self.hp <= damage:
            self.hp = 0
        else:    
            self.hp -= damage
    def takeHeel(self, heel: int):
        if self.hp + heel > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heel

vasia = Player(10)
# print(vasia.hp)
# vasia.takeDamage(5)
# print(vasia.hp)
# vasia.takeHeel(40)
# print(vasia.hp)
# vasia.takeDamage(-100)
# print(vasia.hp)

class User:
    def __init__(self, name: str, age: int, balance: int):
        if name != "":
            self.__name = name
        else:
            self.__name = "не указано"
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
        return self.__name
    #Создание свойства через декоратор property
    @property
    def Balance(self):
        return self.__balance
    #Добавить к свойству Balance setter
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
    #метод снять со счёта
    def take_money(self, money: int):
        if self.__balance - money >= 0 and money > 0:
            self.__balance -= money
    def put_money(self, money: int):
        if money > 0:
            self.__balance += money
    #метод внести на счёт

arkadi = User("Аркадий", 25, 3000)

arkadi.set_name("Акакий")
print(arkadi.get_name())

arkadi.__name = "Акакий"
print(arkadi.__name)

print(arkadi.Balance)
arkadi.Balance = -1000
print(arkadi.Balance)
