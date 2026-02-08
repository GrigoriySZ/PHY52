import asyncio
import time
from multiprocessing import Pool, cpu_count
from os import cpu_count

from wishlist_station import manage_wishlist  # Станция 1
from packing_station import start_packing  # Станция 2
from feeding_station import start_feeding  # Станция 3


def main():
    """Запускает процессы из обработки писем"""

    print('ПРОЦЕСС ПОДГОТОВКИ ПОДАРОКОВ (последовательно): ЗАПУСК')
    start = time.time()

    # Обрабатываем пожелания детей и получаем список пожеланий
    general_wish_list = asyncio.run(manage_wishlist())

    need_food = 0

    gifts = []
    # Упаковываем подарки детей
    for child in general_wish_list:
        gift = [(wish, len(wish)) for wish in child['wishes']]
        gifts.extend(gift)
        need_food += 10
    start_packing(gifts)

    # Кормим оленей в зависимости от
    start_feeding(need_food)

    end = time.time()

    duration = end - start
    print('ПРОЦЕСС ПОДГОТОВКИ ПОДАРОКОВ: ЗАВЕРШЕН')
    print(f'Подготовка подарков к отправке заняла: {duration:.1f} сек.')


if __name__ == '__main__':

    main()