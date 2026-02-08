import os
import time
from functools import wraps


LOG_FILE = 'log_file.txt'
tasks_list = []
completed_tasks_list = {}
last_completed = ''


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Логирует действия пользователя и записывает их в файл 'log_file.txt'"""

        with open(LOG_FILE, 'a', encoding='UTF-8') as log_file:
            try:
                log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: '
                               f'Вызов метода {func.__name__} c аргументами '
                               f'args={args}, kwargs={kwargs}\n')
                result = func(*args, **kwargs)
                log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: '
                               f'Метод {func.__name__} завершил работу'
                               f'и вернул значения: {result}\n')
            except Exception as e:
                log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: '
                               f'Ошибка в функции {func.__name__}: {e}\n')
        return func(*args, **kwargs)
    return wrapper


def add_task():
    """Добавляет задачу в список текущих задач

    Returns:
        new_task (str): Новая задача из списка
    """

    try:
        new_task = input("Введите текст задачи: ").strip()
        if not new_task:
            print('Пустое')  ###
        elif new_task in tasks_list:
            print('Задача уже есть в списке')
        else:
            tasks_list.append(new_task)
            return new_task
    except ValueError:
        print(f'Ошибка ввода!')
    except KeyError:
        print('Ошибка ввода! Текст задачи не может быть пустым.')


def show_current_tasks(full_list: bool = False):
    """Выводит список текущий задач в виде строк и возвращает список с задачами"""

    if tasks_list:
        print(f"Список текущих задач ({len(tasks_list)}):")
        for i, task in enumerate(tasks_list, 1):
            print(f'{i}. {task}')
        return True
    print('Список задач пуст.')
    return False

def show_completed_tusks():
    """Выводит список завершенных задач в виде строк и возвращает список с задачами"""

    if completed_tasks_list:
        print(f"Список завершенных задач ({len(tasks_list)}):")
        for i, task in enumerate(completed_tasks_list, 1):
            print(f'{i}. {task}')
        return True
    print('Список завершенных задач пуст.')
    return False

def complete_task():
    """Завершает выбранную задачу и перемещает её в список готовых задач"""

    if tasks_list:
        show_current_tasks()
        try:
            while True:
                complete = int(input('Для завершения введите номер задачи из списка: '))
                if complete in range(1, len(tasks_list) + 1):
                    index = int(complete - 1)
                    tasks_list.pop(index)
                    last_completed = tasks_list.pop(index)
                    completed_tasks_list.append(last_completed)
                    break
                raise IndexError
            return last_completed, index
        except ValueError:
            print('Ошибка ввода!')
        except KeyError:
            print('Ошибка ввода! Вы не ввели номер задачи для завершения')
        except IndexError:
            print("Задачи с запрашиваемым номером нет в списке.")
    return None



def undo_task():
    """Отменяет последнее выполненное действие"""

    if not completed_tasks_list:
        print('Список выполненных задач пуст.')
        return False
    elif last_completed:
        undo = completed_tasks_list.pop(last_completed)
        last_completed = completed_tasks_list[-1]
        add_task(undo)


def main():
    pass
