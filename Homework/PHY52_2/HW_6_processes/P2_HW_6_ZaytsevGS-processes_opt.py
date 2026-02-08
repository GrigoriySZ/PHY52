import os
import multiprocessing as mp
import threading
import asyncio
import time


TASKS = [n for n in range(1,10001)]
SEPARATION_LINE = '-'*30
PROCESS_LIMIT = mp.cpu_count() // 2


def cpu_tusk(n: int):
    """Вычисляет n-й элемент последовательности Фибоначчи и возвращает значение"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def slow_task(number: int):
    """Имитирует медленное выполнение внешней операции

    Args:
        number (int): Значение вычисления числа из последовательности Фибоначчи

    Returns:
        (int): Итоговое число из последовательности

    """
    print(f'Начинаю вычисление со значением {number}...')
    result = cpu_tusk(number)
    print(f'Результатом вычисления значения {number} = {result} (Процесс: {os.getpid()}).')
    return result

async def slow_task_async(number: int):
    """Имитирует медленное асинхронное выполнение внешней операции

    Args:
        number (int): Значение вычисления числа из последовательности Фибоначчи

    Returns:
        (tuple): Факториал числа и номер процесса, в котором

    """
    print(f'Начинаю вычисление со значением {number}...')
    result = cpu_tusk(number)
    print(f'Результатом вычисления значения {number} = {result} (Процесс: {os.getpid()}).')
    return result

def run_tasks():
    """Имитирует синхронный подход последовательного выполнения задач.

    Returns:
        Возвращает длительность прохождения операций

    """
    print(SEPARATION_LINE)
    print(f'Начало синхронного выполнения задач...')

    # Засекаем начало выполнения операций
    start = time.perf_counter()

    results = []
    for number in TASKS:
        result = slow_task(number)
        results.append(result)

    # Засекаем окончание выполнения операций
    end = time.perf_counter()

    duration = end - start
    print('Окончание синхронного выполнения задач.')
    return duration

def run_tasks_threading():
    """Имитирует многопоточный подход выполнения задач.

    Returns:
        Возвращает длительность прохождения операций

    """
    print(SEPARATION_LINE)
    print(f'Начало многопоточного выполнения задач...')

    # Засекаем начало выполнения операций
    start = time.perf_counter()

    threads = []
    # Создаём потоки для задач
    for task in TASKS:
        thread = threading.Thread(target=slow_task, args=(task,))
        threads.append(thread)
        thread.start()

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    # Засекаем окончание выполнения операций
    end = time.perf_counter()

    duration = end - start
    print('Окончание многопоточного выполнения задач.')
    return duration

def run_tasks_multiprocessing():
    """Имитирует многопроцессорный подход выполнения задач.

    Returns:
        Возвращает длительность прохождения операций

    """
    print(SEPARATION_LINE)
    print(f'Начало многопроцессорного выполнения задач...')

    # Засекаем начало выполнения операций
    start = time.perf_counter()

    # Создаем процессы для задач
    with mp.Pool(processes=PROCESS_LIMIT) as pool:
        results = pool.map(slow_task, TASKS)

    # Засекаем окончание выполнения операций
    end = time.perf_counter()

    duration = end - start
    print('Окончание многопроцессорного выполнения задач.')
    return duration

async def run_tusks_async():
    """Имитирует асинхронный подход выполнения задач.

    Returns:
        Возвращает длительность прохождения операций

    """
    print(SEPARATION_LINE)
    print(f'Начало асинхронного выполнения задач...')

    # Засекаем начало выполнения операций
    start = time.perf_counter()

    # Создаем список задач
    tasks = [slow_task_async(number) for number in TASKS]

    # Запускаем одновременное выполнение задач и дожидаемся результата
    results = await asyncio.gather(*tasks)

    # Засекаем окончание выполнения операций
    end = time.perf_counter()

    duration = end - start
    print('Окончание асинхронного выполнения задач.')
    return duration

def main():
    """Последовательно запускает все подходы выполнения задач и выводит длительность каждого подхода"""

    sync_time = run_tasks()
    thread_time = run_tasks_threading()
    mp_time = run_tasks_multiprocessing()
    async_time = asyncio.run(run_tusks_async())

    print(SEPARATION_LINE)
    print('Общая продолжительность выполнения задач:')
    print(f'Синхронный подход: {sync_time:.1f} сек')
    print(f'Многопоточный подход: {thread_time:.1f} сек')
    print(f'Многопроцессорный подход: {mp_time:.1f} сек')
    print(f'Асинхронный подход: {async_time:.1f} сек')

if __name__ == '__main__':

    # Запускаем основную программу
    main()