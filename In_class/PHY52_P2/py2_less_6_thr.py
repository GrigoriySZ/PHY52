# threads - потоки
# queqe - FIFO - first in first out
# stack - LIFO - last in first out

import threading
import time

# jam = 10

def func():
    print('Задача 1')
    name = threading.current_thread.__name__
    print({name})
    time.sleep(4)
    print('Данные прочитаны')

def func_2():
    print('Задача 2')
    name = threading.current_thread.__name__
    print({name})
    time.sleep(2)
    print('Данные прочитаны')

def main():
    print('Программа запущена')
    s = time.time()
    t1 = threading.Thread(target=func, name='Поток A')
    t2 = threading.Thread(target=func_2, name='Поток B')
    t1.start()
    t2.start()
    print('Ждем завершения')
    t1.join()  # ждем завершения потока
    t2.join() 
    e = time.time()
    print(f'Время выполнения: {e-s}')

# main()

# Состояние гонки
# У потока есть понятие "Гонка данных". Такое возникает, когда несколько потоков работают с одной переменной. 
# Из-за этого эффекта могут возникнуть недостоверные результаты
jam = 10
lock = threading.Lock() 

def use_jam(name):
    global jam
    # Захватываем замок: только один поток может работать
    with lock:
        if jam > 0:
            time.sleep(0.1)
            jam -= 1
            print(jam)
        else:
            print('Джем закончился')

def main():
    threads = []
    for i in range(12):
        t = threading.Thread(target=use_jam, args=(f'поток{i}',))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f'Финальное количество: {jam}')


main()