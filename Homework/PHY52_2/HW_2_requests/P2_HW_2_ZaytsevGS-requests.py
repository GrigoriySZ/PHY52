import requests
import json

TEACHER_NOTES = '''
+++ JYP  должно быть JPY 
+++ в get_valute_by_code дважды проверяется наличие валюты
но если валюты нет в CURRENT_VALUTA, но есть в API   
её нельзя будет получить, хотя функционально это возможно
--- нет обработки ввода пустой строки в некоторых местах
например, в show_exchange_rate() при вводе кода валюты
Логика повторного ввода немного запутана
в get_choice_to_convert() есть вложенные циклы while, что усложняет чтение
Ошибка при вводе нечисловой суммы
Есть обработка TypeError, но лучше ловить ValueError для float(). '''

# Ссылка на публичное API для получения курса валют.
API_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
# CURRENT_VALUTA = ['USD', 'EUR', 'JPY', 'GBP', 'CNY', 'CHF', 'AUD', 'CAD']

currencies = {'RUB': {
    "ID": "R00001",
    "NumCode": "643",
    "CharCode": "RUB",
    "Nominal": 1,
    "Name": "Российский рубль",
    "Value": 1.0,
    "Previous": 1.0
    }
}

def request_currencies():
    """Отправляем запрос к API и десериализирует данные"""

    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Проверяем наличие данных по запросу к API
        if data:
            currencies.update(data['Valute'])
            return True
        return False

    # Обрабатываем ошибки модулю requests в области подключения
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return False

    # Обрабатываем ошибку обработки ответа
    except json.JSONDecodeError:
        print('JSON decode error!')
        return False

def get_valute_by_code(char_code: str):
    """Выдает словарь с курсом валюты по коду валюты

    Parameters:
        char_code (str): Код валюты в виде трех латинских букв

    Returns:
        dict: Словарь с названием, единицами и курсом валюты к рублю
    """

    if char_code not in currencies:  ###
        return None
    currency = currencies[char_code]
    value = currency['Value']
    nominal = currency['Nominal']
    name = currency['Name']
    rate_unit = value/nominal
    return {
        'value': value,
        'nominal': nominal,
        'name': name,
        'code': char_code,
        'rate_unit': rate_unit
    }

def show_exchange_rate():
    """Выводит на терминал текущий курс валюты по запросу пользователя в виде строки

    Returns:
        str: Вывод на терминал текущего курса валюты по запросу пользователя
    """

    try:
        # Запрашиваем у пользователя код валюты для вывода курса этой валюты к рублю RUB
        while True:
            show_currencies_list()
            char_code = input('Введите код валюты для вывода курса: ').strip().upper()
            if char_code in currencies:
                valuta = get_valute_by_code(char_code)
                if valuta:
                    print(f'| Текущий курс {valuta["name"]} ({char_code}) к рублю (RUB):')
                    print(f'| Единиц: {valuta["nominal"]}, Курс: {valuta["value"]:.2f}')
                    break
            print('Ошибка ввода команды!')
            while True:
                choice = input('Хотите ввести запрос ещё раз (да/нет): ').strip().lower()
                if choice == 'нет':
                    return input()
                elif choice == 'да':
                    break
                else:
                    print('Ошибка ввода команды. ')
        print('Нажмите Enter для возвращения в меню')
        return input(':')
    except KeyError:
        print('Ошибка ввода! Строка не должна быть пустой')


def get_choice_to_convert():
    """Запрашивает у пользователя валюты и сумму для конвертации,
        выводит на терминал конвертированную сумму.

        Returns:
            str: Количество денежных единиц после конвертации
        """

    currencies = request_currencies()
    change_from = None
    change_to = None
    amount = 0
    repeat = True

    try:
        # Запрашиваем у пользователя исходную конвертируемую валюту
        while True:
            while True:
                show_currencies_list()
                if not change_from:
                    change_from = str(input('Введите код конвертируемой валюты: ')).strip().upper()
                    if change_from in currencies:
                        print(f'Конвертация из {change_from}...')
                    else:
                        print('Ошибка! Выбранной валюты нет в списке! ')
                        change_from = None
                        break

                # Запрашиваем у пользователя валюту для конвертации
                if not change_to:
                    change_to = str(input('Нажмите Enter для конвертации в рубли (RUB) '
                                          'или введите код валюты: ')).strip().upper()
                    if change_to == '':
                        change_to = 'RUB'
                        print(f'Конвертация из {change_from} в {change_to}.')
                    elif change_to in currencies:
                        print(f'Конвертация из {change_from} в {change_to}.')
                    else:
                        print('Ошибка! Запрашиваемой валюты для конвертации нет в списке. ')
                        break

                # Запрашиваем у пользователя конвертируемую сумму
                if not amount:
                    amount = float(input('Введите сумму для конвертации: '))
                    if amount <= 0:
                        print('Ошибка! Сумма для конвертации не может быть отрицательной или нулевой')
                        amount = 0
                    elif amount > 0:
                        print(f'Конвертация из {change_from} в {change_to}: {amount}.')
                        repeat = False
                        break

            while repeat:
                choice = input('Хотите ввести запрос ещё раз (да/нет): ').strip().lower()
                if choice == 'нет':
                    print('Отмена выбора! Нажмите Enter для возвращения в меню.')
                    return input(':')
                elif choice == 'да':
                    break
                else:
                    print('Ошибка ввода команды! ')
            else:
                break

    except TypeError:
        print('Ошибка ввода! Введите сумму в числовом виде.')
    except KeyError:
        print('Ошибка ввода! Вы не ввели значение запроса.')
    except ValueError:
        # При неправом запросе уточняем у пользователя о повторном запросе
        print('Ошибка ввода команды')

    convert_currencies(change_from, change_to, amount)
    print('Нажмите Enter для возвращения в меню.')
    return input(':')


def convert_currencies(change_from: str, change_to: str, amount: float):
    """Производит конвертацию валюты

    Parameters:
        change_from (str): Код конвертируемой валюты
        change_to (str): Код валюты для конвертации
        amount (float): Величина конвертируемой валюты

    Returns:
        str: Количество денежных единиц после конвертации
    """

    valute_from = get_valute_by_code(change_from)
    if change_to == 'RUB':
        converted_amount = amount * (valute_from['value']/valute_from['nominal'])
        print(f'{amount:.2f} {valute_from['code']} = {converted_amount:.2f} RUB')
    else:
        valute_to = get_valute_by_code(change_to)
        converted_amount = (amount * (valute_from['value'] / valute_from['nominal']) /
                            (valute_to['value'] / valute_to['nominal']))
        print(f'{amount:.2f} {valute_from['code']} = {converted_amount:.2f} {valute_to['code']}')


def show_currencies_list(limit: int = 10):
    """Выводит пользователю список валют для определения курса

    Parameters:
        limit (int): Определяет максимальное число выводимых валют (default: 10)
    """

    print('Доступные валюты:')
    sorted_currencies = sorted(currencies.items(), key=lambda x: x[1]['Nominal'])
    for i, (char_code, currency) in enumerate(sorted_currencies[:limit], start=1):
        print(f'| {i}. {char_code}: {currency["Name"]}')


def main_menu():
    """Меню для взаимодействия с пользователем.

    Предоставляет выбор операций с валютами и выводит результат на терминал.
    Доступные функции:
    1. Просмотр курса выбранной валюты
    2. Конвертация валюты
    """

    request_currencies()
    try:
        while True:
            print('\nВыберите действие:')
            print('| 1. Посмотреть курс валюты')
            print('| 2. Конвертировать валюту')
            print('| 3. Показать список валют')
            print('| 4. Обновить данные')
            print('| 0. Выйти')

            choice = input('Ваш выбор: ').strip()
            if choice == '1':
                show_exchange_rate()
            elif choice == '2':
                get_choice_to_convert()
            elif choice == '3':
                show_currencies_list()
            elif choice == '4':
                request_currencies()
            elif choice == '0':
                print('Программа завершена. ')
                break
            else:
                print('Некорректный выбор. ')
                input('Нажмите Enter для продолжения')
    except KeyboardInterrupt:
        print('Программа завершена. ')

main_menu()


