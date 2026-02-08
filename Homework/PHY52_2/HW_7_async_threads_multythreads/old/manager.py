import threading
import time
import multiprocessing
from wishlist_station import manage_wishlist  # Станция 1
from packing_station import start_packing  # Станция 2
from feeding_station import start_feeding  # Станция 3

def main():
    """Запускает процессы из обработки писем"""

    print('ПРОЦЕСС ПОДГОТОВКИ ПОДАРОКОВ: ЗАПУСК')
    start = time.time()

    children_names = manage_wishlist()
    start_packing(children_names)
    start_feeding()

    end = time.time()
    duration = end - start
    print('ПРОЦЕСС ПОДГОТОВКИ ПОДАРОКОВ: ЗАВЕРШЕН')
    print(f'Подготовка подарков к отправке заняла: {duration} сек.')


if __name__ == '__main__':

    main()