import os
from datetime import datetime
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with open("logs.txt", "a", encoding="UTF-8") as file:
            try:
                file.write(f"{datetime.now()}: Вызов метода '{func.__name__}' в {self.__class__.__name__} "
                           f"с аргументами args={args}, kwargs={kwargs}\n")
                result = func(self, *args, **kwargs)
                file.write(f"{datetime.now()}: Метод '{func.__name__}' завершил работу "
                           f"и вернул значение: {True if args else False}\n")
                return result
            except Exception as e:
                file.write(f"Ошибка в функции {func.__name__}: {e}\n")
    return wrapper


class FinanceManager:
    """Менеджер по учёту финансов"""

    def __init__(self):
        self.__balance = 0.00
        self.__transactions = []

    @log
    def add_transaction(self, type_ta: str, amount_ta: float, category_ta: str):
        """Добавляет новую транзакцию (доход\расход),
        обновляет баланс и сохраняет данные в историю"""
        if type_ta == "доход":
            self.__balance += amount_ta
        else:
            self.__balance -= amount_ta
        self.__transactions.append({"type": type_ta, "amount": amount_ta, "category": category_ta})
        print(f"|- Транзакция: {type_ta.capitalize()} в объеме {amount_ta:.2f} "
              f"c категорией '{category_ta.capitalize()}' успешно добавлена.")

    @property
    def transaction(self):
        """Возвращает список всех транзакций"""
        return self.__transactions

    @property
    def balance(self):
        """Возвращает текущий баланс"""
        return self.__balance

    def save_data(self):
        """Сохраняет денные в текстовый файл"""
        with open("transactions.txt", "w", encoding="UTF-8") as f:
            f.write(f"balance:{self.__balance}")
            for ta in self.__transactions:
                f.write(f"\n{ta["type"]},{ta["amount"]},{ta["category"]}")
        print("|- Данные успешно сохранены!")

    def load_data(self):
        """Загружает данные из текстового файла"""
        if os.path.exists("transactions.txt"):
            with open("transactions.txt", "r", encoding="UTF-8") as file:
                for index, line in enumerate(file):
                    if index == 0:
                        first_line = line.split(":")
                        self.__balance = float(first_line[1])
                    else:
                        type_ta, amount_ta, category_ta = line.replace("\n", "").split(",")
                        self.__transactions.append({"type": type_ta,
                                                    "amount": float(amount_ta),
                                                    "category": category_ta})
            print("Данные успешно загружены.")
        else:
            print("Файл данных не найден! Начинаем с пустого баланса")

    def run(self):
        """Запускает алгоритм взаимодействия с пользователем"""
        self.load_data()

        while True:
            menu = (f"Меню: \n"
                    f"| 1. Добавить доход/расход\n"
                    f"| 2. Показать баланс и транзакции\n"
                    f"| 3. Сохранить и выйти\n"
                    f"Выберите номер действия: ")
            try:
                answer = int(input(menu))
            except ValueError:
                print("|- Ошибка ввода! Введите числовое значение")
                continue

            # 1. Добавить доход/расход
            if answer == 1:
                while True:
                    type_ta = input("| Введите тип транзакции (доход/расход): ").lower()
                    if type_ta in ("доход", "расход"):
                        break
                    else:
                        print("|- Неверный ввод!")
                try:
                    while True:
                        amount_ta = float(input("| Введите величину транзакции: "))
                        if amount_ta < 0:
                            print("|- Ошибка! Введите положительное число")
                        elif amount_ta > self.__balance and type_ta == "расход":
                            raise ValueError
                        else:
                            break
                except TypeError:
                    print("|- Ошибка! Введите числовое значение")
                except ValueError:
                    print("|- Ошибка! Недостаточно средств на балансе")
                    continue
                while True:
                    category_ta = input("| Введите категорию транзакции: ").lower()
                    if category_ta != "":
                        break
                    else:
                        print("|- Ошибка! Введите категорию транзакции")
                self.add_transaction(type_ta, amount_ta, category_ta)

            # Показать баланс и транзакции
            elif answer == 2:
                print("Баланс и транзакции: ")
                print(f"| Текущий баланс: {float(self.__balance):.2f}")
                for index, ta in enumerate(self.__transactions, 1):
                    print(f"| {index}. Тип: {ta["type"]}; Количество: {ta["amount"]:.2f}; "
                          f"Категория: {ta["category"]}")

            # 3. Сохранить и выйти
            elif answer == 3:
               self.save_data()
               print("|- До свидания!")
               break

            # Обработка неправильного ввода команды
            else:
                print("|- Ошибка ввода команды!")


my_manager = FinanceManager()
my_manager.run()