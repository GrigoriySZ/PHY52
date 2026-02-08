import os
import multiprocessing
from multiprocessing import Pool, cpu_count

def pack_gift(gift_name: str, complexity: int):
    """Упаковываем подарки

    Arguments:
        gift_name (str): Название подарка
        complexity (int): Число для имитации работы упаковки

    Returns:
        complexity (float): Имитирует сложность упаковки
        
    """
    pid = os.getpid()
    print(f'ПРОЦЕСС {pid}. Упаковка: {gift_name}')
    result = 0
    limit = complexity * 10**5
    for i in range(limit):
        result += i * i
    print(f'ПРОЦЕСС {gift_name}|{pid}|УПАКОВАН')
    return complexity

def start_packing(wishes_queue: multiprocessing.Queue, 
                  num_workers: int | None=None):
    """Запускает процессы упаковки подарков
    
    Arguments:
        wishes_queue (multiprocessing.Queue): Очередь для получения данных от wishlist_station
        feeding_queue (multiprocessing.Queue): Очередь для передачи объемов еды в feeding_station
        num_workers (int): Указывает ограничение задействованных процессов (Default=None)

    """
    print('СТАНЦИЯ 2: ЗАПУСК')

    while True:
        
        # Получаем список подарков из очереди
        gift_list = wishes_queue.get()

        # Завершаем цикл при получении сигнала
        if gift_list == 'DONE':
            break
        
        # Определяем количество процессов для упаковки подарка
        if num_workers is None: 
            num_workers = min(len(gift_list), cpu_count())  # Задаем ограничение пула процессов
        print(f'{num_workers} рабочих процессов')
        
        with Pool(processes=num_workers) as pool:  # Запускаем пул процессов
            pool.starmap(pack_gift, gift_list)

    print('СТАНЦИЯ 2: ЗАВЕРШЕНИЕ РАБОТЫ')

if __name__ == '__main__':

    in_queue = multiprocessing.Queue()
    
    test_gift_list = [
        ('Наушники', 5),
        ('Плюшевый мишка', 9),
        ('Телескоп', 4),
    ]

    in_queue.put(test_gift_list)
    in_queue.put('DONE')

    start_packing(in_queue)

