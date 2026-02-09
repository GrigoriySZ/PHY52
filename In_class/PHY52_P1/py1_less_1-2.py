# # \n (new line) - новая строка
# # \t (tab) - неразрывный пробел
# # \" - вставить кавычку
# # \\ - вставить слэш
# print("привет", "\"пока\"", sep=";", end="\n")

# # цикл whilt - цикл с условием
# count = 0
# while count < 10: 
#     print(count)
#     count += 1

# answer = str.lower(input("Введи слово \"баклажан\":\n"))
# while answer != "баклажан":
#     answer = str.lower(input("Я же простил ввести \"баклажан\":\n"))

# # цикл for - итерративный алгоритм
# # для каждого i в диапазоне до 10 
# range(5) -> 0, 1, 2, 3, 4;    i = 0, i < 5; i += 1
# range(5, 10)                  i = 5, i < 10; i += 1 
# range(5, 10, 2)               i = 5, i < 10; i += 2
# for i in range(10, 0, -1):
#     print(i)

# numbers = [4, 6, 2, 1, -5, 0, -2]
# summ = 0
# # способ через индексы
# for index in range(0, len(numbers), 1):
#     summ += numbers[index]
#     print(index, summ, sep=": ")
# print(summ / len(numbers))

# sum(numbers) - функция sum() хранит внутри себя вышенаписанный цикл for index

# # способ перебора
# for element in numbers: 
#     summ += element
#     print(summ)
# print(summ / len(numbers))

# # линейный поиск
# elements = [2, 6, 3, 0, -11, 22, 11, 20, 4]
# max_element = elements[0]
# for i in range(1, len(elements)):
#     if elements[i] > max_element:
#         max_element = elements[i]
# print(max_element)

# # max(numbers) - функция max() ищет максимальное значение списка, перебирая его линейным поиском

questions = [
    "Сколько иголок у ежа?",
    "Какой язык мы изучаем?"
    ]
right_answers = [
    "101",
    "python"
    ]

for index in range(len(questions)):
    answer = input(questions[index])
    if answer == right_answers[index]:
        print("Вы ответили правильно!")
    else:
        print("Вы ошиблись!")
