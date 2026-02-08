'''
Задача N1.
Создать исходный список.
Написать алгоритм, который создаст новый список,
содержащий только четные числа из исходного списка.
'''

# Создаем список с числами от 1 до 10
numbers = [n for n in range(1, 10)]
print(numbers)

# Создаем пустой список под четные числа
even_number = [n for n in numbers if n % 2 == 0]
print(even_number)

# # Заполняем список четных чисел значениями из исходного списка
# for index in range(len(numbers)):
#     if numbers[index] % 2 == 0:
#         even_number.append(numbers[index])
# else:
#     print(even_number)


'''
Задача N2
Развернуть список без использования встроенной функции reverse().
'''

# # Обращаем список четных чисел слайсом и записываем в новый список
# reversed_list = even_number[::-1]
# print(reversed_list)

reversed_numbers = [n for n in even_number[::-1]]
print(reversed_numbers)