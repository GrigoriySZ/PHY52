import os 
import asyncio
import multiprocessing
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

async def check_wishlists(child_name: str, delay: float):
    """Асинхронно проверяет списки поежалния детей и выдаёт список с пожеланиями
    
    Arguments: 
        child_name (str): Имя ребенка для проверки списка пожеланий
        delay (float): Задержка для имитации длительного чтения файла

    Returns:
        wishlist (list): Список подарков от одного ребенка
    
    """
    file_path = os.path.join(WISHLIST_DIR, f'{child_name.lower()}_list.txt')
    print(f'Начинаем считывание пожелания {child_name} из файла {file_path}')
    
    # Начинаем считывать
    try: 
        await asyncio.sleep(delay)
        with open(file_path, 'r', encoding='UTF-8') as file:
            content = file.read()
            wishlist = [line.split('.')[1].strip() for line in content.splitlines()
                        if line.startswith(tuple('1234'))]
            num_wishes = len(wishlist)
        print(f'ASYNC: {child_name}: Список проверен. Найдено {num_wishes} пожеланий.')
        return wishlist
    except FileNotFoundError:
        print(f'{file_path} не найден')
        return []
    except Exception as e:
        print(f'ERROR: {e}')
        return []

async def manage_wishlist(packing_queue: multiprocessing.Queue,
                          feeding_queue: multiprocessing.Queue):
    """Асинхронно запускает задачи
    
    Arguments:
        queue (multiprocessing.Queue): Очередь для передачи результатов станции упаковки

    """
    print('СТАНЦИЯ 1: ЗАПУСК')

    children_names = get_child_name()  # Получаем имена детей
    
    # Проверяем списки детей поочередно и отправляем результат в очередь
    for child in children_names:
        delay = random.uniform(0.5, 2.0)
        wishlist = await check_wishlists(child, delay)
        complexibility = [random.randint(1, 5) for _ in range(len(wishlist))]
        gift_list = list(zip(wishlist, complexibility))
        need_food = sum(complexibility)
        await asyncio.to_thread(packing_queue.put, gift_list)
        await asyncio.to_thread(feeding_queue.put, need_food)
    
    # Сигнал о завершении работы
    await asyncio.to_thread(packing_queue.put, 'DONE')
    await asyncio.to_thread(feeding_queue.put, 'DONE')

    print('СТАНЦИЯ 1: ЗАВЕРШЕНИЕ РАБОТЫ')

# Проверочный запуск скрипта
if __name__ == '__main__':
    
    packing_queue = multiprocessing.Queue()
    feeding_queue = multiprocessing.Queue()

    asyncio.run(manage_wishlist(packing_queue, feeding_queue))