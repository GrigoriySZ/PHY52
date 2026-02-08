import asyncio
import time
import multiprocessing
from wishlist_station import manage_wishlist  # Станция 1
from packing_station import start_packing  # Станция 2
from feeding_station import start_feeding  # Станция 3


async def main():
    """Запускает процессы из обработки писем"""

    print('ПРОЦЕСС ПОДГОТОВКИ ПОДАРОКОВ: ЗАПУСК')
    start = time.time()
    
    processes = []

    # Создаем процесс по упаковке подарков
    wishes_queue = multiprocessing.Queue()
    feeding_queue = multiprocessing.Queue()

    packing_process = multiprocessing.Process(target=start_packing,
                                      args=(wishes_queue,))
    packing_process.start()
    processes.append(packing_process)
    
    # Создаем процесс по кормлению оленей
    feeding_process = multiprocessing.Process(target=start_feeding,
                                              args=(feeding_queue,))
    feeding_process.start()
    processes.append(feeding_process)

    # Обрабатываем пожелания детей и получаем список пожеланий
    await manage_wishlist(wishes_queue, feeding_queue)

    for process in processes:
        process.join()

    end = time.time()

    duration = end - start
    print('ПРОЦЕСС ПОДГОТОВКИ ПОДАРОКОВ: ЗАВЕРШЕН')
    print(f'Подготовка подарков к отправке заняла: {duration:.1f} сек.')


if __name__ == '__main__':

    multiprocessing.set_start_method('spawn')
    asyncio.run(main())