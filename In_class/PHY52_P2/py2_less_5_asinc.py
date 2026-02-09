# asyncio - встроенная библиотека для асинхронной работы
# корутины - асинхронные функции
# конкурентное выполнение - не параллельное

import asyncio
import time

# async def - объявление корутины через async перед обьявлением функции
# await - 'подожди здесь'
# 
# time.sleep() - останавливает работу скрипта и не позволяет работать асинхронно
# asyncio.sleep() - асинхронная версия

# def make_coffee():
#     print('Начинаем варить кофе')
#     time.sleep(3)
#     print('Кофе готов!')


# def make_tost():
#     print('Начинаем делать тосты')
#     time.sleep(2)
#     print('Тосты готовы!')

# start_time = time.time()
# make_coffee()
# make_tost()
# end_time = time.time()
# print(f'Синхронное: {end_time - start_time}')


# async def make_coffee_async():
#     print('Начинаем варить кофе')
#     await asyncio.sleep(3)
#     print('Кофе готов!')

# async def make_tost_async():
#     print('Начинаем делать тосты')
#     await asyncio.sleep(2)
#     print('Тосты готовы!')

# async def main():
#     start_time = time.time()
#     await asyncio.gather(make_coffee_async(), make_tost_async())  #Одновременный запуск 
#     end_time = time.time()
#     print(f'Асинхронное: {end_time - start_time}')

# asyncio.run(main())

# tasks (задачи) - автономные асинхронные задачи, работающие независимо друг от друга
# create_task() - метод для создания задач

async def heavy_task(name, delay):
    print(f'Запуск {name} началась (займет {delay})')
    await asyncio.sleep(delay)
    print(f'Завершина {name}')
    return f'Результат {name}'

async def main():
    start = time.time()
    task1 = asyncio.create_task(heavy_task('Кофе', 3))
    task2 = asyncio.create_task(heavy_task('Тосты', 2)) 
    await asyncio.sleep(1)
    result1 = await task1
    result2 = await task2
    end = time.time()
    print(f'Time: {end - start}')
    print(f'Итого: {result1}, {result2}')

asyncio.run(main())