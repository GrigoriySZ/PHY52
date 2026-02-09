# Декораторы - функции-обертки, которые оборачивают базовую функцию, 
# улучшают её функцилона
# Обращение декоратора происходит через @

import time
import hashlib
import json
import os
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Внутренний docstring"""
        print('Начало выполнения декораторка')
        return func(*args, **kwargs)
    return wrapper

#*args - агрументы
# **kwargs - именованные агрументы/

def func(*args, **kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)

# Порядок передачи параметров:
# 1. Обящательные агрументы 
# 2. Аргументы по умолчания 
# 3. *args 
# 4. **kwargs
# func(c=5, a=9, s='t', k='q', f=9.0, z=0, n=None, b=True)

# python -m venv .venv - команда для создания виртуального окружения в текущей дериктории
# .\.venv\Scripts\activate - команда для активации виртуального пространства (venv)
# dir - команда, показывающая все файлы в текущей дериктории
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass - команда для отключения скриптов на время

# Метаданные функции
# __name__ - поле имени функции
# __doc__ - поле документации

@decorator
def test():
    '''Исходный docstring'''
    pass

# print(test.__name__)
# print(test.__doc__)

# Метод time() показывает текущее время от начала в формате количества секунд от начала отчёта
print(time.time()) 

# Метод sleep останавливает исполнение скрипта на заданное время секунд
time.sleep(2)
time_now = time.time()
time_from = f'Seconds: {round(time_now)}; minutes: {round(time_now/60)}; hours: {round(time_now/3_600)}; \
    days: {round(time_now/86_400)}; years: {round(time_now/31_557_600)}'

print(time_from)

# Создание своего исключения TimeError
class TimeError(Exception):
    pass

def time_checker(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            sub_time = end_time - start_time
            if sub_time > limit:
                raise TimeError(
                    f'Функция "{func.__name__}" превысила лимит '
                    f'(выполнилась за {sub_time:.2f} сек.)'
                )
            return res
        return wrapper
    return decorator


@time_checker(limit=2)
def fast_operation(n):
    time.sleep(1)
    return f'Операция завершина успешно'

@time_checker(limit=0.5)
def slow_operator(n):
    time.sleep(1)
    return f'Операция завершина успешно'

try:
    mess = fast_operation(100)
    print(mess)
except TimeError as e:
    print(f'Error: {e}')

try:
    mess = slow_operator(100)
    print(mess)
except TimeError as e:
    print(f'Error: {e}')

# hash - хранение данные
# cache - данные

# SHA256 - 64 символа

CACHE_FILE = 'cache.json'

def load_cache():
    '''Загружает данные из кэш файла'''
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='UTF-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print('Файл поврежден или пуст')
            return {}
    return {}

def save_cache(data):
    '''Сохраняет данные в кэш файл'''
    with open(CACHE_FILE, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=4)

def archivaruis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''Архивируем данные фанкции в кэш'''
        # Проверяем возможность получения данных
        try:
            # Получаем аргументы
            args_string = json.dumps([args, kwargs], sort_keys=True)
        except TypeError as e:
            print(f'Ошибка сериализации аргументов: {e}')
            return func(*args, **kwargs)
        
        # хэшируем 
        hasher = hashlib.sha256()
        hasher.update(args_string.encode('UTF-8'))
        cache_key = hasher.hexdigest()  # Шестнадцатиричная строка

        # Загружаем данные из кэша
        cache = load_cache()

        # Проверяем наличие ключа к кэше
        if cache_key in cache:
            print('Результат из кэша')
            return cache[cache_key]
        
        # Если данных нет в кэше, то мы исполняем функцию
        res = func(*args, **kwargs)
        
        # Добавляем результат функции в кэш и созраняем
        cache[cache_key] = res
        save_cache(cache)
        return res
    return wrapper


@archivaruis
def calculate_cache(a, b, wait_time=2):
    time.sleep(wait_time)
    return a*b + sum(range(a))

def calculate_uncache(a, b, wait_time=2):
    time.sleep(wait_time)
    return a*b + sum(range(a))



def main():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
    
    # FIRST долгое без кэша
    s_t = time.time()
    res1 = calculate_cache(10, 5, 1)
    e_t = time.time()
    print(f'Result: {res1}')
    print(f'Time: {e_t - s_t}')

    # SECOND повторное с теми же аргументами (с кэшем) 
    s_t = time.time()
    res1 = calculate_cache(10, 5, 1)
    e_t = time.time()
    print(f'Result: {res1}')
    print(f'Time: {e_t - s_t}')

    # THIRD c новыми аргументами 
    s_t = time.time()
    res1 = calculate_cache(20, 3, 1.5)
    e_t = time.time()
    print(f'Result: {res1}')
    print(f'Time: {e_t - s_t}')

    # FOURTH с теми же аргументами (с кэшем) 
    s_t = time.time()
    res1 = calculate_cache(20, 3, 1.5)
    e_t = time.time()
    print(f'Result: {res1}')
    print(f'Time: {e_t - s_t}')

    # FIFTH без декоратора архиватора
    s_t = time.time()
    res1 = calculate_uncache(20, 3, 1.5)
    e_t = time.time()
    print(f'Result: {res1}')
    print(f'Time: {e_t - s_t}')

    # SIXTH повторный без декоратора с теми же аргументами
    s_t = time.time()
    res1 = calculate_uncache(20, 3, 1.5)
    e_t = time.time()
    print(f'Result: {res1}')
    print(f'Time: {e_t - s_t}')


main()