import requests
import json


# Ссылка на публичное API для получения курса валют.
API_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


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

    char_code = char_code.upper()
    if char_code not in currencies:
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
    print('Просмотр курса обмена валюты')
    show_currencies_list()
    # Запрашиваем у пользователя код валюты для вывода курса этой валюты к рублю RUB
    while True:
        char_code = input('Введите код валюты для вывода курса (USD, RUB и т.д.): ').strip().upper()
        if not char_code:
            print('Ошибка ввода! Вы не ввели значение.')
        elif char_code in currencies:
            valuta = get_valute_by_code(char_code)
            if valuta:
                print(f'| Текущий курс {valuta["name"]} ({char_code}) к рублю (RUB):')
                print(f'| Единиц: {valuta["nominal"]}, Курс: {valuta["value"]:.2f}')
                print(f'| Курс за 1 {char_code}: {valuta["rate_unit"]} RUB')
                break
        else:
            print(f'Валюты "{char_code}" нет в списке.')
    input('Нажмите Enter для продолжения')

def get_choice_to_convert():
    """Запрашивает у пользователя валюты и сумму для конвертации,
        выводит на терминал конвертированную сумму.

        Returns:
            str: Количество денежных единиц после конвертации
        """

    change_from = None
    change_to = None
    amount = 0.0

    # Запрашиваем у пользователя исходную конвертируемую валюту
    show_currencies_list()
    while True:
        if not change_from:
            change_from = str(input('Введите код конвертируемой валюты (USD, RUB и т.д.): ')).strip().upper()
            if not change_from:
                print('Ошибка ввода! Вы не ввели код конвертируемой валюты. ')
            elif change_from not in currencies:
                print(f'Ошибка! Валюты "{change_from}" нет в списке! ')
                change_from = None
            continue

        # Запрашиваем у пользователя валюту для конвертации
        if not change_to:
            change_to = str(input('Введите код для конвертации (USD, RUB и т.д.): ')).strip().upper()
            if not change_to:
                print('Ошибка ввода! Вы не ввели код валюты для конвертации.')
            elif change_to not in currencies:
                print(f'Ошибка! Валюты "{change_to}" нет в списке!')
                change_to = None
            elif change_to == change_from:
                print(f'Ошибка! Вы пытаетесь перевести "{change_from}" в "{change_to}"!')
                change_to = None
            continue

        # Запрашиваем у пользователя конвертируемую сумму
        try:
            if amount <= 0:
                amount = float(input('Введите сумму для конвертации: '))
                if amount <= 0.0:
                    print('Ошибка! Конвертируемая сумма не может быть отрицательной или нулевой')
                    amount = 0.0
                elif amount > 0.0:
                    print(f'| Конвертация из {change_from} в {change_to}: {amount}.')
                    break
        except ValueError:
            print('Ошибка ввода! Введите числовое значение.')

    convert_currency(change_from, change_to, amount)
    input('Нажмите Enter для продолжения')

def convert_currency(change_from: str, change_to: str, amount: float):
    """Производит конвертацию суммы amount из change_from в change_to

    Parameters:
        change_from (str): Код конвертируемой валюты
        change_to (str): Код валюты для конвертации
        amount (float): Величина конвертируемой валюты
    """

    valute_from = get_valute_by_code(change_from)
    valute_to = get_valute_by_code(change_to)
    converted_amount = (amount * valute_from['rate_unit'] / valute_to['rate_unit'])
    print(f'| {amount:.2f} {valute_from['code']} равняется {converted_amount:.2f} {valute_to['code']}')


def show_currencies_list(limit: int = 10, full_list: bool = False):
    """Выводит пользователю список валют для определения курса

    Parameters:
        limit (int): Определяет максимальное число выводимых валют (default: 10)
        full_list (bool): При True показывает выводит полный список валют (default: False)
    """

    print('Доступные валюты:')
    sorted_currencies = sorted(currencies.items(),
                               key=lambda x: x[1]['Value']/x[1]['Nominal'], reverse=True)

    # Определяем величину выводимого списка
    if len(sorted_currencies) < limit or full_list:
        limit = len(sorted_currencies)

    # Выводим список валют
    for i, (char_code, currency) in enumerate(sorted_currencies[:limit], start=1):
        print(f'| {i}. {char_code}: {currency["Name"]}')

    # Выводим числом количество возможных валют
    if len(sorted_currencies) > limit:
        counter_of_hidden_currencies = len(sorted_currencies) - limit
        print(f'Ещё {counter_of_hidden_currencies} валют...')


def main_menu():
    """Меню для взаимодействия с пользователем.

    Предоставляет выбор операций с валютами и выводит результат на терминал.
    Доступные функции:
    1. Просмотр курса выбранной валюты
    2. Конвертация валюты
    3. Показывает список валют
    4. Обновить данные
    """

    data = request_currencies()

    if data:
        try:
            while True:
                print('\nВыберите действие:')
                print('| 1. Посмотреть курс валюты')
                print('| 2. Конвертировать валюту')
                print('| 3. Показать список валют')
                print('| 4. Обновить данные')
                print('| 0. Выйти')

                choice = input('Выберите действие: ').strip()
                if choice == '1':
                    show_exchange_rate()
                elif choice == '2':
                    get_choice_to_convert()
                elif choice == '3':
                    show_currencies_list(full_list=True)
                    input('Нажмите Enter для продолжения')
                elif choice == '4':
                    request_currencies()
                elif choice == '0':
                    print('Программа завершена. ')
                    break
                else:
                    print('Некорректный выбор. ')
                    input('Нажмите Enter для продолжения')
        except KeyboardInterrupt:
            print('\nПрограмма завершена. ')

main_menu()