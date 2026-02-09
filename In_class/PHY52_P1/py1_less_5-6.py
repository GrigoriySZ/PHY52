
'''
# Функции (definitive or def) - способ создать именованный блок кода
# DRY - don't repeat yourself 


# Параметры функции выглядят в виде переменных, которые объявляются в её определении
# value1: int - аннотация типов
# Аннотации типов обязательно всегда для удобства чтения
# Аннотации типов возвращающей функции не обязателя 
# Оператор return передает какой-то результат
# Функция не обязана что-то возвращать

def summator(value1: int|float, value2: int|float) -> int|float:
    return value1 + value2
   

res = summator(5, )
summator(18, 6)
a = 10 
b = 15
summator(a, b)
summator()


# Итератор (iterator)

test_list = [1, 2, 3]
it = iter(test_list)  # Функция iter() определяет итератор
print(next(it))  # Функция next() вызывает срабатывание итератора и переводит итератор на сделующий шаг
print(next(it))
# Итератор - это объект, позволяющий переберать коллекции. 

# Генератор (generator)

# Параметры по дефолту - имеют стандартное значение 
# на место такого параметра можно не передавать аргумент.
# Дефолтные параметры должны быть в конце после всех обязательных

def my_range(start: int, end: int, step: int = 1):
    current = start
    while current < end:
        yield current
        current += step

# Именованная передача аргументов
# my_range(1, 10, 2) - упорядоченная передача аргументов
# my_range(end=10, start=1, step=2) - именованная передача агрументов
# my_range(1, 10, step=2) - гибридный тип передачи параметров

# for i in my_range(end=10, start=1, step=2):
#     print(i)
# int - 4 Б
# float - 8 Б
# bool - 1 Б
# ссылка - 8 Б
# !!! Все примитивы передаются как копии, остальные типы как ссылки !!!
# reference type - ссылочный тип/ типы, на которые передаются ссылкой
# value type - значимый тип/типы, которые копируются при передаче

def function(value):
    value += 10 
    print(value)

def function_2(lst):
    new_lst = list(lst)
    new_lst.append(10)

var = 5
function(5)
print(var)

test_list = [1, 2, 3]
# создание ссылки на список
lst2 = test_list
lst2.append(5)
# создание нового списка на основе старого через функцию list()
lst3 = list(test_list)
lst3.append(10)
print(test_list)
# function_2(test_list)
# print(test_list)


# Функции и модули (библиотеки)
# случайные числа
# способы подключения модуля (библиотеки):
# 1 - подключить random 
import random  
r1 = random.randint(1, 5)
# 2 - подключить random как rd
import random as rd
r2 = rd.randint(1, 5)
# 3 - из random подключить как всё (* - all)
from random import *
r3 = randint(1, 5)
# 4 - из random подключить определенную функцию
from random import randint
r4 = randint(1, 5)

# Библиотеки подключаются до их приминения.
# Импорты принято писать первыми строчками.

print(r1, r2, r3, r4)
print(rd.choice([42, 5, 6, 2, 1, 7, -1, 44]))
'''
import math

print(math.sqrt(5125))
print(5125 ** 0.5)

# Для установки нестандартных модуля на win можно использовать библиотеку pip
# pip install numpy
import numpy

import lib

print(lib.summator(5, 2))