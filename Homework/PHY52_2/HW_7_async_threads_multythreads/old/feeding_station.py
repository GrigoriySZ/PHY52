import time
import threading
import random

def feed_reindeer(reindeer_name: str, food_amount: int, time_to_eat: int):
    """Кормит оленя едой заданное время.
     
    Arguments:
        reindeer_name (str): Имя оленя для кормления
        food_amount (int): Количество еды для кормления оленя
        time_to_eat (int): Время кормления оленя
    
    """
    thread_name = threading.current_thread().name
    print(f'ПОТОК: {reindeer_name} | {thread_name}. Начало')
    time.sleep(time_to_eat)
    print(f'ПОТОК: {reindeer_name} | {thread_name}. Готово')


def start_feeding(reindeer_list: list):
    """Запускает кормление оленей """

    print('СТАНЦИЯ 3: ЗАПУСК')
    threads = []

    # Задаем и запускаем потоки 
    for name, food in reindeer_list:
        time_to_eat = random.uniform(1.0, 3.0)
        thread = threading.Thread(
            target=feed_reindeer,
            args=(name, food, time_to_eat),
            name=f'Feeder-{name}'
        )
        threads.append(thread)
        thread.start()
    
    # Вызываем ожидание окончания потоков
    for thread in threads:
        thread.join()

    print('СТАНЦИЯ 3: ЗАВЕРШЕНИЕ РАБОТЫ')

if __name__ == '__main__':

    test_reindeer_list = [
        ('Comet', 10),
        ('Dancer', 5),
        ('Rudolf', 7)
    ]
    
    start_feeding(test_reindeer_list)