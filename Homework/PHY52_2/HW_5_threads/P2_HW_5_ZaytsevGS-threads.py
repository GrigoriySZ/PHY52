import threading
import time

# Список пользователей для отправки уведомлений
USERS = [
    ('Alice', 2),
    ('Bob', 3),
    ('Charlie', 1),
    ('Diana', 4),
    ('Emma', 5),
    ('Frank', 2),
    ('George', 3)
]

SEPARATION_LINE = '-' * 30

def send_notification(username: str, delay: int):
    """Имитирует отправку уведомления пользователю

    Args:
        username (str): Имя пользователя для отправки уведомления
        delay (int): задержка для имитации отправки уведомления
    """

    print(f'\tОтправляю уведомление пользователю {username}...')
    time.sleep(delay)
    print(f'\tПользователь {username} получил уведомление.')

def main():
    """Основная функция программы для отправки уведомлений пользователям"""

    print('Программа для отправки уведомлений запущена...')
    print(SEPARATION_LINE)
    print('Отправка уведомлений: ')

    # Базовый список для записи потоков
    threads = []
    start_time = time.time()

    # Создаём потоки для каждого пользователя из списка пользователей
    for username, delay in USERS:
        thread = threading.Thread(target=send_notification, args=(username, delay))
        threads.append(thread)
        thread.start()

    print('\nОтчет о получении:', end='')
    # Запускаем ожидание завершения работы для каждого потока
    for thread in threads:
        thread.join()

    end_time = time.time()
    duration = int(end_time - start_time)

    print('Все уведомления доставлены!')
    print(SEPARATION_LINE)
    print(f'Программа завершила работу за {duration} сек.')

if __name__ == '__main__':
    main()