import time
import random
import os
from multiprocessing import Pool, cpu_count


def pack_gift(gift_name: str, complexity: int):
    """Упаковываем подарки

    Arguments:
        gift_name (str): Имя получателя подарка
        complexity (int): Число для имитации работы упаковки

    """
    pid = os.getpid()
    print(f'ПРОЦЕСС {pid}. Упаковка: {gift_name}')
    result = 0
    limit = complexity * 10**7
    for i in range(limit):
        result += i * i

    print(f'ПРОЦЕСС{gift_name}|{pid}|УПАКОВАН')
    return f'{gift_name} упакован с {result % 100}'

def start_packing(gift_list: list, num_workers: int=None):
    """Запускает процессы упаковки подарков
    
    Arguments:
        gift_list (list): Список подарков
        num_workers (int): Указывает ограничение задействованных процессов (Default=None)

    """
    print('СТАНЦИЯ 2: ЗАПУСК')
    
    if num_workers is None:
        num_workers = min(len(gift_list), cpu_count())  # Задаем ограничение пула процессов
    print(f'{num_workers} рабочих процессов')
    
    with Pool(processes=num_workers) as pool:  # Запускаем пул процессов
        # gift_list = [(Name, complexity)]
        result = pool.starmap(pack_gift, gift_list)

    print('СТАНЦИЯ 2: ЗАВЕРШЕНИЕ РАБОТЫ')

if __name__ == '__main__':
    test_gift_list = [
        ('Наушники', 5),
        ('Плюшевый мишка', 9),
        ('Телескоп', 4)
    ]

    start_packing(gift_list=test_gift_list)