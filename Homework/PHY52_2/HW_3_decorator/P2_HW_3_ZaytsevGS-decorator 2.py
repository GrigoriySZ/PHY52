import os
import time
from functools import wraps


LOG_FILE = 'log_file.txt'


def log_action(func):
    @wraps(func)
    def wrapper(self,*args, **kwargs):
        """Логирует действия пользователя и записывает их в файл 'log_file.txt'"""

        with open(LOG_FILE, 'a', encoding='UTF-8') as log_file:
            try:
                result = func(self,*args, **kwargs)
                log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: '
                               f'Вызван метод {func.__name__} в {self.__class__.__name__} '
                               f'c аргументами args={args}, kwargs={kwargs} '
                               f'и вернул значения: {result}\n')
                return result
            except Exception as e:
                log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: '
                               f'Ошибка в функции {func.__name__}: {e}\n')
    return wrapper


class TaskManager:
    """Менеджер задач

    """

    def __init__(self):
        self.tasks_list = []
        self.completed_tasks_list = []
        self.last_completed = tuple()
    
    @log_action
    def add_task(self):
        """Добавляет задачу в список текущих задач"""

        new_task = self.input_task()

        if new_task:
            self.tasks_list.append(new_task)
            print(f'| Задача "{new_task}" добавлена в список задач')
            input('Нажмите Enter для продолжения. ')
            return new_task
        print('Не удалось добавить задачу')
        input('Нажмите Enter для продолжения. ')
        return False      


    def input_task(self):
        """Запрашивает у пользователя текст задачи
        
        Returns: 
            new_task (str): Возвращает текст задачи  
        """
        
        try:
            while True:
                new_task = input("Введите текст задачи: ").strip().capitalize()
                if new_task == '':
                    print('Ошибка ввода! Текст задачи не может быть пустым')
                    return False
                elif new_task in self.tasks_list:
                    print('| Задача уже есть в списке')
                    return False
                return new_task
        except ValueError:
            print(f'Ошибка ввода!')
            input('Нажмите Enter для продолжения. ')
        except KeyError:
            print('Ошибка ввода! Текст задачи не может быть пустым.')
            input('Нажмите Enter для продолжения. ')


    def show_current_tasks(self):
        """Выводит список текущий задач в виде строк и возвращает список с задачами"""

        print(f"Список текущих задач ({len(self.tasks_list)}):")
        if self.tasks_list:
            for i, task in enumerate(self.tasks_list, 1):
                print(f'| {i}. {task}')
            return True
        print('| Список текущих задач пуст')
        return False

    def show_completed_tusks(self):
        """Выводит список завершенных задач в виде строк и возвращает список с задачами"""

        print(f"Список завершенных задач ({len(self.completed_tasks_list)}):")
        if self.completed_tasks_list:
            for i, task in enumerate(self.completed_tasks_list, 1):
                print(f'| {i}. {task[1]}')
            input('Нажмите Enter для продолжения. ')
            return True
        print('| Список завершенных задач пуст')
        input('Нажмите Enter для продолжения. ')
        return False

    @log_action
    def complete_task(self):
        """Завершает выбранную задачу и перемещает её в список готовых задач"""

        if self.tasks_list:
            self.show_current_tasks()
            try:
                while True:
                    to_complete = int(input('Для завершения задаче введите номер из списка: '))
                    
                    # Проверяем пустую строку
                    if not to_complete:
                        print('Вы ввели пустое поле.')

                    elif to_complete < 0:
                        print('Номер задачи должен быть положительным')

                    # Переводим задачу из списка действующих в список завершенных задач.
                    # Обновляет поле последней задачи
                    elif to_complete in range (1, (len(self.tasks_list))+1):
                        index = int(to_complete - 1)
                        completed_task = str(self.tasks_list.pop(index))
                        self.last_completed = (index, completed_task)
                        self.completed_tasks_list.append(self.last_completed)
                        print(f'| Задача "{completed_task}" помечена как выполненная')
                        input('Нажмите Enter для продолжения. ')
                        return completed_task

                    # Обрабатываем неправильный ввод
                    else:
                        print('Задачи с таким номером нет в списке!')
            except ValueError:
                print('Ошибка ввода! Введите числовое значение.')
            except KeyError:
                print('Ошибка ввода! Вы не ввели номер задачи для завершения.')
            except IndexError:
                print("Задачи с запрашиваемым номером нет в списке.")
        print('Cписок текущих задач пуст')
        return False

    @log_action
    def undo_task(self):
        """Отменяет последнее выполненное действие"""

        # Проверяем наличие элементов в списке завершенных задач
        if not self.completed_tasks_list:
            print('Список выполненных задач пуст.')
            return False

        # Переносим значение из списка завершенных в список действующих задач.
        # Обновляем поле последней завершенной задачи
        index, task = self.last_completed
        print(f'| {index}. {task}')
        self.last_completed = self.completed_tasks_list.pop()
        self.tasks_list.insert(index, task)
        if task in self.completed_tasks_list:
            print(f'| Завершение задачи {task} отменено. Задача возвращено в список активных задач')
            return task
        print('Не удалось завершить задачу')
        return False


    def main(self):
        """Главное меню взаимодействия с пользователем"""

        choice = ''

        try: 
            while True:
                print('Ваш личный менеджер задач:')
                print('| 1. Добавить задачу')
                print('| 2. Показать список задач')
                print('| 3. Завершить задачу')
                print('| 4. Отменить последнюю выполненную задачу')
                print('| 0. Выход')

                choice = input('\nВведите номер действия: ').strip()

                if choice == '1':
                    self.add_task()
                elif choice == '2':
                    self.show_current_tasks()
                    self.show_completed_tusks()
                elif choice == '3':
                    self.complete_task()
                elif choice == '4':
                    self.undo_task()
                elif choice == '0':
                    print('\nПрограмма завершена. ')
                    break
                else:
                    print('Ошибка ввода команды! ')

        except KeyboardInterrupt:
            print('Программа завершена.')


manager = TaskManager()
manager.main()