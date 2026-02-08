import os 
import asyncio
import time
import random

WISHLIST_DIR = 'wishlists'


def get_child_name():
    """Возвращает имена отправивших пожелания детей"""

    # Базовый список для добавления имен детей
    children_names = []

    # Проверяем является ли путь директорией
    if not os.path.isdir(WISHLIST_DIR):
        print(f'Ошибка, папка {WISHLIST_DIR} не найдена')
        return children_names
    
    # Поочередно записываем имена из названия файлов
    for file in os.listdir(WISHLIST_DIR):
        if file.endswith('_list.txt'):
            name = file.replace('_list.txt', '')
            child_name = name.capitalize()
            children_names.append(child_name)
    return children_names

async def check_wishlists(child_name, delay):
    file_path = os.path.join(WISHLIST_DIR, f'{child_name.lower()}_list.txt')
    print(f'Начинаем считывание пожелания {child_name} из файла {file_path}')
    
    # Начинаем считывать
    try: 
        await asyncio.sleep(delay)
        with open(file_path, 'r', encoding='UTF-8') as file:
            content = file.read()
            wishlist = [line for line in content.splitlines() if line.startswith(tuple('1234'))]
            num_wishes = len(wishlist)
        print(f'ASYNC: {child_name}: Список проверен. Найдено {num_wishes} пожеланий.')
    except FileNotFoundError:
        print(f'{file_path} не найден')
    except Exception as e:
        print(f'ERROR: {e}')

async def manage_wishlist():
    """Асинхронно запускает задачи"""

    print('СТАНЦИЯ 1: ЗАПУСК')

    children_names = get_child_name()  # Получаем имена детей
    tasks = []  # Пустой список задач
    for child in children_names:
        delay = random.uniform(0.5, 2.0)
        task = check_wishlists(child, delay)  # 
        tasks.append(task)
    
    await asyncio.gather(*tasks)

    print('СТАНЦИЯ 1: ЗАВЕРШЕНИЕ РАБОТЫ')

# Проверочный запуск скрипта
if __name__ == '__main__':
    asyncio.run(manage_wishlist())