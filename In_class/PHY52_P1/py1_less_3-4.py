'''

# break - оператор прерывания цикла

var = 5
while var > 0:
    if var == 3:
        break
    print(var)
    var -= 2

test_list = [5, 2, 15, 0, -7, 22.2, -15]
find_number = 0

for i in range(len(test_list)):
    print(test_list[i], end="; ")
    if test_list[i] == find_number:
        print(f"\nИскомое число {find_number} было найдено под индексом {i}.")
        break

while True:
    num = int(input("Введите \"3\": "))
    if num == 3:
        break

# continue - переводит цикл к следующему повторению. Прерывает текущее повторение

for i in range(1, 10):
    if i % 2 == 1:
        continue
    print(i)

# Пример цикла без использования continue
for i in range(2, 10, 2):
    print(i)

# tuple (кортеж) - неизменяемый список
# Кортеж обьявляется через круглые сколби, но остальные операции происходят через квадратные
tuple_test = (5, 2, 3)
print(tuple_test[0])
# tuple.count() - считает количество искомых значений в кортеже
print(tuple_test.count(5))
# tuple.index() - выдает индекс элемента, на котором находится искомое число. Если искомых элементов нет, то выдает -1

# Сложности алгоритма (асимптотические сложности алгоритма)

# Способы получения сортируемых данных
# Хэша таблица
# Бинарное дерево

# Множество и словарь
# Множество - набор значений в виде бинарного дерева (?)
# Словариь - хранит в себе значения и ключевое слово, по которому можно вызвать значение

# set - множество
test_set = {1, 5, -10, 0, 11}
test_set_2 = {5, 65, 0, 12, 77}
test_set.add(9)
test_set.remove()  # Удаление по значению
test_set.pop()  # Удаление поcледний добавленный элемент
print(test_set.intersection(test_set_2))
print(test_set & test_set_2)
print(test_set.difference(test_set_2))
print(test_set - test_set_2)
print(test_set.union(test_set_2))
print(test_set | test_set_2)

# Словарь (Dictionary - dict) = {key1: value1, key2: value2}
# Value может принимать любые значения, Key может быть только str(), int(), float()
dict_numbers = {"356-751": "Иван", "284-165": "Василий"}
dict_numbers["284-165"] = "Ольга"
print(dict_numbers["284-165"])
for i in dict_numbers.items():
    if i[1] == "Иван":
        print(i[0])

# Если данные упорядочены, то мы выбираем list[]
# Если данных много и порядок не важен, то мы выбираем множества set{}
# Если set{} не подходит, то мы выбираем dict{}
# list - список
# set - сножества
# tuple - кортеж
# dict - словарь

# Преобразование
test_list = [1, 2, 3]
s = set(test_list)
print(s)

# Создание 
lst = list([1, 2, 3])
st = set([1, 2, 3])
tp = tuple([1, 2, 3])
print(lst, st, tp)


test_list = [1, "Вася", 2.55]

# Если list может хранить любой тип данных, 
# то list может хранить внутри себя list, 
# т.к. list тоже является типом данных

test_list = [[1, 2], [6, 7]]
# функция принт выводит 1-й элемент 2-го вложенного списка из списка test_list
print(test_list[1][0])

test_list[0].append(5)
# добавляем 5 в первый вложенный список
print(test_list)

Число типа str() можно разделить порядки при помощи "_" для удобства чтения. 
При обработке этого числа "_" будет игнорироваться

# Список словарей
product_list = [
    {"Название": "Холодильник", "Цена": 35_000, "Вес": 42.7},
    {"Название": "Микроволновка", "Цена": 5_000, "Вес": 6.4},
    {"Название": "Телевизор", "Цена": 42_000, "Вес": 5.2},
    {"Название": "Пылесос", "Цена": 7_800, "Вес": 2.8}
]

# Вывксти название товаров, которые дороже 8000
for product in product_list:
    if product["Цена"] > 8000:
        print(product["Название"])

# "в" in "василий"
# 5 in [2, 7, 5]
# Вывксти товары, название которых подходит
for product in product_list:
    if "ик" in product["Название"].lower():
        print(f"Товар - {product["Название"]}\nЦена - {product["Цена"]}")

# print(product_list[2]["Название"])  # При обращение к словарю мы вместо индекса обращаемся по ключу словаря
# print(product_list[2]["Название"], product_list[2]["Цена"])

temp_data = {
    "Температура": [-7, -5, -5, -4, -3, -3, -4, -5, -8, -8, -9, -10],
    "Восход": "09:55",
    "Текущая температура": -5
}

summ = 0
for temp in temp_data["Температура"]:
    summ += temp
avg_temp = summ / len(temp_data["Температура"])
# Фильтр к дробному числу {float:.2f} ограничивает количество символов и округляет вниз
print(f"Средняя температура за день: {avg_temp:.2f}")  


# Определить простое число

number = int(input("Введите число: "))
if number == 2:
    print("число простое")
elif number == 1 or number == 0:
    print("Число не простое и не составное")
elif number % 2 == 0: 
    print("Число составное")
else:
    # for - else
    # если цикл не был прерван break, то выполнится код
    # внутри else
    for i in range(3, number // 2 + 1, 2):
        if number % i == 0:
            print("число составное")
            break
    else:
        print("простое")
    # print("простое" if isPrime else "составное")
    # if isPrime:
    #     print("число простое")
    # else:
    #     print("число составное")

'''

test_list = [5, 2, 3, 4, 5, 1, 8]
new_list = []

for item in test_list:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)

# Генератор списков (list comprehension)
# Генерирует список из test_list только четными элементами 
new_list_generator = [x for x in test_list if x % 2 == 0]
print(new_list_generator)

# Создает новый список с умножением всех числе на 2
# new_list_generator = [x * 2 for x in test_list]

# Задача со списками списков

dif_list = [[1, 5], [2, 4], [3, 8]]
# Выводим список из первых элементов каждого вложенного списка
print([e[0] for e in dif_list if e[1] % 2 == 0])
