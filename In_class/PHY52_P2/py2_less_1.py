# user: startsoft, pass: 424242
# Для установки библиотек pip install (lib_name)

# Работа с файлами в Python
# Read
# Открываем соединения
# file = open("test.txt")  
# Закрываем соединения
# file.close()

# Контекстный менеджер with автоматически вызываем метод close() и егр не нужно прописывать вручную
# Элиас as будет определять переменную для файла, чтобы обращаться к нему в будущем
# "w" (write) - перезапись файла
# "r" (read) - чтение файла
# "a" (append) - дозапись файла
with open("test.txt", "a", encoding="UTF-8") as file:
    file.writelines(["a", "b", "c"])
    # write() записывает только строки
    # writelines() записывает список строк (только строки)

file_path = ""

if os.path.exists(file_path):
    with open("example.txt", "r", encoding="UTF-8") as file:
        print(file.read())
        list_stroke = []
        for line in file.readlines():
            list_stroke.append(line.strip())
        print(list_stroke)


if os.path.exists(file_path):
    with open("example.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(f"- {line}")

import os

# Относительный путь файла - файл от места расположения скрипта
# Абсолютный путь файла - полный путь файла в системе
file_path = "example.txt"

if os.path.exists(file_path):
    with open("example.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(f"- {line}")
else:
    print("file not found")

try:
    with open("example.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(f"- {line}")
except FileNotFoundError as e:
    print(f"Error: {e}")

# Формат JSON - Java Script O

dict_ = {"a": 1, "b": 2, "c": 3}
json_s = '{"a": 1, "b": 2, "c": 3}'
# в JSON ключи всегда вписаны в двойные ковычки

import json
# Сериализация - процесс перевода py объекта в другой объект
# dump() - считывание из json файла
# dumps() - будет работать со строкой
print(json.dumps(dict_))
print(type(json.dumps(dict_)))

# Десериализация - процесс перевода другого объекта в py объект
# load() - запись в json файл
# loads() - будет работать со строкой
print(json.loads(json_s))
print(type(json.loads(json_s)))

with open('data.json', 'w', encoding='UTF-8') as f:
    json.dump(dict_, f, indent=4, ensure_ascii=False)
    # Первые 2 параметра обязательны для заполенния
    # Параметр indent (отступ) нужен для отображения читаемой структуры
    # Параметр ensure_ascii=False позволяет правильно отображать кириллицу
print('Данные сохранены')

with open('data.json', 'r', encoding='UTF-8') as f:
    loaded_data = json.load(f)
print(loaded_data)
print(type(loaded_data))

# Запросы на удаленный сервер 
# get() - метод запроса на сервер 
# post() - метод на создание чего-то на сервере

import requests as rq
api_url = 'https://official-joke-api.appspot.com/random_joke'
response = rq.get(api_url)

if response.status_code == 200:
    joke_data = response.json()  
    '''Автоматически превратили json строку в словарь'''
    print(joke_data)
    print(type(joke_data))
    print(f'Начало: {joke_data["setup"]}\nРазвязка: {joke_data["punchline"]}')
elif response.status_code == 429:
    error = response.json()
    print(f'Ошибка: {error['message']}')
else:
    print(f'Статус код: {response.status_code}')