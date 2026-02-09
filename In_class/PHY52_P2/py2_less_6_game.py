import asyncio
import threading
import time
import random
import msvcrt
import os


FIELD_WIDTH = 80
FIELD_HEIGHT = 20
ROW_SHIP = FIELD_HEIGHT - 1  # индекс строки для передвижения корабля (самый низ)
SCORE_TO_WIN = 100

class Game:
    """Хранит и управляет состоянием игрового поля и объектов"""

    def __init__(self):
        self.ship_x = FIELD_WIDTH // 2
        self.asteroids = set()  # Позиция астероидов
        self.bullet = set()  # Позиция снаряда 
        self.score = 0
        self.win = False
        self.is_running = True

    def add_bullets(self, x, y):
        """Создает новый снаряд над кораблём"""

        self.bullet.add((x, y))


    def add_asteroids(self, x, y):
        """Создает новый астероид"""

        self.asteroids.add((x, y))

    def move_ship(self, direction):
        """Двигает корабль влево и вправо"""

        if direction == 'LEFT':
            # self.ship_x() = max(0, self.ship_x-1)
            if self.ship_x < 0:
                self.ship_x = FIELD_WIDTH-1
            self.ship_x -=1

        elif direction == "RIGHT":
            # self.ship_x() = max(FIELD_WIDTH-1, self.ship_x+1)
            if self.ship_x > FIELD_WIDTH - 1:
                self.ship_x = 0
            self.ship_x += 1

class InputThread(threading.Thread):
    """Поток для считывания пользовательского ввода"""

    def __init__(self, command_queue):
        super().__init__()
        self.command_queue = command_queue
        self._running = True  # Для управления циклом потока
        self.daemon = True  # Поток-демон для автоматического завершения

    def run(self):
        """Основной цикл потока ввода"""

        while self._running:
            if msvcrt.kbhit():
                try:    
                    key = msvcrt.getch().decode('cp866', errors='ignore').upper()  #
                except:
                    try:
                        key = msvcrt.getch().decode('UTF-8', errors='ignore').upper()
                    except:
                        key = msvcrt.getch().upper()
                
                command = None
                if key in ('A', 'Ф'):
                    command = 'LEFT'
                elif key in ('D', 'В'):
                    command = 'RIGHT'
                elif key == ' ':
                    command = 'FIRE'
                elif key in ('Q', 'Й'):
                    command = 'QUIT'
                
                if command:
                    try:
                        self.command_queue.put_nowait(command)
                    except:
                        pass  # Игнорирует переполение очереди
                    # asyncio.run_coroutine_threadsafe(
                    #     self.command_queue.put(command), 
                    #     asyncio.get_event_loop())
        
        time.sleep(0.01)  # Задержка для избежания 100% загрузки
    
    def stop(self):
        self._running = False


# асинхронные корутины (задачи)
async def input_handle(game, command_queue): 
    while game.is_running:

        try:
            # неблокирующее получение команды из очереди
            command = command_queue.get_nowait()
        except asyncio.QueueEmpty:
            await asyncio.sleep(0.01)
            continue

        if command == 'LEFT' or command == 'RIGHT':
            game.move_ship(command)
        elif command == 'FIRE':
            game.add_bullets(game.ship_x, ROW_SHIP-1)
        elif command == 'QUIT':
            game.is_running = False
        command_queue.task_done() 

# async def move_object(game, obj_type, initial_pos, delay):
#     x, y = initial_pos
#     if obj_type == 'bullet':
#         game.bullet.add((x, y))
#         direction = -1
#     elif obj_type == 'asteroid':
#         game.asteroids.add((x, y))
#         direction = 1
#     else:
#         return
#     while game.is_running and 0 <= y < FIELD_HEIGHT:
#         await asyncio.sleep(delay)
#         new_y = y + direction
#         old_pos = (x, y)
#         new_pos = (x, new_y)
#         # обновляем множества
#         if obj_type == 'asteroid':
#             game.asteroids.discard(old_pos)  # discard(x) - удаляет x значение из множества
#             if 0 <= new_y < FIELD_HEIGHT:
#                 game.asteroids.add(new_pos)
#         elif obj_type == 'bullet':
#             game.bullet.discard(old_pos)
#             if 0 <= new_y < FIELD_HEIGHT:
#                 game.bullet.add(new_y)

#         y = new_y 
#         if obj_type == 'asteroid' and y >= FIELD_HEIGHT:
#             game.is_running = False
#             break

async def move_bullets(game):
    '''отдельная корутина для движения всех снарядов'''
    while game.is_running:
        bullets_to_move = list(game.bullet)
        bullets_to_remove = set()
        bullets_to_add = set()
        
        for x, y in bullets_to_move:
            new_y = y - 1  # Движение вверх
            if new_y >= 0:
                bullets_to_remove.add((x, y))
                bullets_to_add.add((x, new_y))
            else:
                bullets_to_remove.add((x, y))
        
        # Обновляем множества снарядов
        game.bullet -= bullets_to_remove
        game.bullet.update(bullets_to_add)
        
        await asyncio.sleep(0.05)  # задержка движения снарядов

async def move_asteroids(game):
    '''отдельная корутина для движения всех астероидов'''
    while game.is_running:
        asteroids_to_move = list(game.asteroids)
        asteroids_to_remove = set()
        asteroids_to_add = set()
        
        for x, y in asteroids_to_move:
            new_y = y + 1   
            if new_y < FIELD_HEIGHT:
                asteroids_to_remove.add((x, y))
                asteroids_to_add.add((x, new_y))
            else:
                asteroids_to_remove.add((x, y))

                if new_y >= ROW_SHIP:
                    game.is_running = False
        
        # обновляем множества астероидов
        game.asteroids -= asteroids_to_remove
        game.asteroids.update(asteroids_to_add)
        
        await asyncio.sleep(0.5)  # задержка движения астероидов

async def generate_asteroids(game):
    ASTEROID_DELAY = 1.0  # Задержка между появлениями астероидов
    ASTEROID_MOVE_DELAY = 0.5  # Задержка для движения одного астеороида

    while game.is_running:
        x = random.randrange(0, FIELD_WIDTH)
        y = 0
        game.add_asteroids(x, y)
        await asyncio.sleep(ASTEROID_DELAY)

async def draw_field(game):
    """Отрисовывает поле, проверяет коллизии"""

    DRAW_DELAY = 0.05  # Задержка между кадрами 20 кадров в секунду
    BULLET_MOVE_DELAY = 0.08  # Задержка движения снаряда

    while game.is_running:
        os.system('cls')
        # 1. проверка коллизий и обновление счёта
        bullet_to_remove = set()
        asteroid_to_remove = set()
        for bx, by in game.bullet:
            for ax, ay in game.asteroids:
                if bx == ax and by == ay:
                    bullet_to_remove.add((bx, by))
                    asteroid_to_remove.add((ax, ay))
                    game.score += 10
                    break
        game.bullet -= bullet_to_remove
        game.asteroids -= asteroid_to_remove

        ship_collision = False  # Флаг столкновения корабля
        for ax, ay in game.asteroids:
            if ay == ROW_SHIP and ax == game.ship_x:
                ship_collision = True
                break

        if ship_collision:
            game.is_running = False

        if game.score >= SCORE_TO_WIN:
            game.is_running = False
            game.win = True

        field = []
        for row in range(FIELD_HEIGHT):
            line = []
            for col in range (FIELD_WIDTH):
                if row == ROW_SHIP and col == game.ship_x:
                    line.append('^')  # Корабль
                elif (col, row) in game.asteroids:
                    line.append('*')  # астероид
                elif (col, row) in game.bullet:
                    line.append('|')  # Снаряд
                else:
                    line.append(' ')  # свободное пространство
            field.append(''.join(line))
        print('\n'.join(field))
        print(f'Счет: {game.score} | Цель: {SCORE_TO_WIN}')
        print(f'Управление: A/Ф - влево, D/B - вправоб, ПРОБЕЛ - выстрел')
        print(f'Астеоридов: {len(game.asteroids)}')
        print(f'Снарядов: {len(game.bullet)}')

        await asyncio.sleep(DRAW_DELAY)

async def main():
    game = Game()
    command_queue = asyncio.Queue()  # Очередь

    input_thread = InputThread(command_queue)
    input_thread.start()  # Запустк потока

    # Запуск асинхронных задач
    try:
        tasks = [
            asyncio.create_task(input_handle(game, command_queue)),
            asyncio.create_task(generate_asteroids(game)),
            asyncio.create_task(move_bullets(game)),
            asyncio.create_task(move_asteroids(game)), 
            asyncio.create_task(draw_field(game))
        ]
        while game.is_running:  # Ждем завершения игры
            await asyncio.sleep(0.1)

        for task in tasks:
            task.cancel()  # Отмена всех задач
        await asyncio.gather(*tasks, return_exceptions=True)

    except KeyboardInterrupt:
        game.is_running = False
    finally:
        input_thread.stop()  # Остановка потока ввода
        input_thread.join(timeout=1)
    
    os.system('cls')
    if game.win:
        print(f'ПОБЕДА! Вы набрали {game.score} очков')
    else:
        print(f'WASTED! Ваш счет: {game.score}')
        
if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nИгра завершина пользователем')