# Задача N1
# Подсчет элементов.
# Создать исходный список и запросить искомое число.
# Посчитать, сколько раз искомый элемент встречается в списке.


# Задаем список элементов
numbers = [-31, -33, 2, 22, 16, 8, 6, 5, 3, -1, 1, -9, 32]

start = True
while start:
    try:
        find_number = int(input("Введите искомое целое число: "))  # Запрашиваем искомое число у пользователя
        if find_number in numbers:  # Проверяем наличие числа в списке
            count_number = numbers.count(find_number)
            # Число есть в списке
            print(f"Искомое число \"{find_number}\" в списке встречается: {count_number} раз.")
        else:
            # Числа нет в списке
            print(f"В списке нет числа \"{find_number}\".")
    except ValueError:
        print("Ошибка! Неверный запрос.")
    finally:
        answer = ""
        while answer != "да" and answer != "нет":
            # Запрашиваем повторный поиск
            answer = str.lower(input("Хотите продолжить поиск? Да/Нет \n:"))
            if answer == "да":
                continue
            elif answer == "нет":
                start = False
            else:
                print("Неправильный ввод! Введите ответ \"Да/Нет\" ")

# Задача N2
# Поиск второго наименьшего элемента.
# Найти второй по величине элемент в списке.

# Объявляем переменные
min_number = numbers[0]
second_min_number = numbers[1]

# Определяем первое и второе наименьшее число
for i in range(1, len(numbers)):
    if numbers[i] < min_number or numbers[i] < second_min_number:
        if numbers[i] < min_number:
            # second_min_number = min_number
            # min_number = numbers[i]
            second_min_number, min_number = min_number, numbers[i]
        else:
            second_min_number = numbers[i]
        print(f"{i}: {min_number}, {second_min_number}")
print(f"Второе наименьшее число из списка: {second_min_number}")

# Задача N3
# Проверка на палиндром.
# Определить, является ли список палиндромом (элементы читаются одинаково слева направо и справа налево).
# Например, [5, 2, 1, 0, 0, 1, 2, 5], учтите, что размер списка может быть нечётным

palindrome = [5, 2, 1, 0, 1, 2, 5]  # Задаем палиндром
is_palindrome = False

for i in range(len(palindrome) // 2):
    if palindrome[i] == palindrome[-i - 1]:
        is_palindrome = True
    else:
        is_palindrome = False
        break
else:
    if len(palindrome) // 2 == 0:
        is_palindrome = True


if is_palindrome:
    print("Список является палиндромом.")
else:
    print("Список не является палиндромом.")


# Задача N4
# Возведение в степень.
# Запросить два числа: основание и степень.
# Возвести основание в указанную степень, пользуясь только циклом.
# Встроенные функции для возведения в степень использовать не нужно.

# Запрашиваем у пользователя число и степень для возведения
while True:
    try:
        num = int(input("Введите число для возведения в степень: "))
        power = int(input("Введите степень возведения числа: "))
        break
    # Обрабатываем ошибку неправильного ввода числа и степени
    except ValueError:
        print("Неверный ввод! Введите целое число.")

# Объявляем переменную для возведения в степень
power_num = num
for i in range(1, power):
    power_num *= num
print(f"{num} ^ {power} = {power_num}")