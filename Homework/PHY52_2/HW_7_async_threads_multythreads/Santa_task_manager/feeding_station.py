import time
import threading
import random

reindeers_list = [
    'Dashing',
    'Dancer', 
    'Prancer',
    'Vixen',
    'Comet',
    'Cupid',
    'Doner',
    'Blitzen'
]

def feed_reindeer(reindeer_name: str, food_amount: int, time_to_eat: int):
    """Кормит оленя едой заданное время.
     
    Arguments:
        reindeer_name (str): Имя оленя для кормления
        food_amount (int): Количество еды для кормления оленя
        time_to_eat (int): Время кормления оленя
    
    """
    thread_name = threading.current_thread().name
    print(f'ПОТОК: {reindeer_name} | Еда: {food_amount} | {thread_name}. Начало')
    time.sleep(time_to_eat)
    print(f'ПОТОК: {reindeer_name} | Еда: {food_amount} | {thread_name}. Готово')


def start_feeding(food_need: int):
    """Запускает кормление оленей 
    
    Arguments:
        food_need (int): Необходимое количество еды
    """

    print('СТАНЦИЯ 3: ЗАПУСК')
    threads = []

    # Задаем и запускаем потоки 
    for name in reindeers_list:
        time_to_eat = random.uniform(1.0, 3.0)
        food = food_need / len(reindeers_list)
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

    test_reindeer_list = 50
    
    start_feeding(test_reindeer_list)