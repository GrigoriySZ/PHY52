import requests
import json
import os

# ссылка
API_URL = 'https://api.jamendo.com/v3.0/tracks/'
LIMIT = 10
MOOD_TAGS = {
 '1': ('радостное', 'pop'),
 '2': ('спокойное', 'chill'),
 '3': ('энергичное', 'rock'),
 '4': ('грустное', 'ambient'),
 '5': ('сосредоточенное', 'classical'),
}

CLIENT_ID = '25aece0e'

def request_tracks(params: dict):
    # &format=json&limit=10&tags=chill&audiodlformat=mp31
    default_params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': LIMIT,
        'audioformat': 'mp31'
    }
    # 
    full_params = {**default_params, **params}
    try:
        response = requests.get(API_URL, params=full_params)
        response.raise_for_status()
        data = response.json()
        if data ['headers']['status'] == 'success':
            return data['results']
        else:
            print(f'Error: {data['headers']['error_message']}')
            return []
    # Обрабатывает ошибки модуля requests в области подключения 
    except requests.exceptions.RequestException as e:
        print(e)
    except json.JSONDecodeError:
        print('Ошибка обработки ответа')
        return []
    
def display_tracks_get_choiсe(tracks: dict):
    if not tracks:
        print('Треки не найдены')
        # print('Введите "Enter" для продолжения')
        # input('')
        return None
    print('Найденные композиции: ')
    display_list = []
    for i, track in enumerate(tracks):
        title = track.get('name', 'название неизвестно')
        artist = track.get('artist_name', 'неизвестный артист')
        print(f'{i+1}. {title} - {artist}')
        display_list.append(track)
    print('M - чтобы вернуться в меню')
    while True:
        choise = input(f'Введите номер трека или "М" для выхода: ').strip().lower()
        if choise == 'm':
            return None  # сигнал о возврате в меню
        try: 
            t_i = int(choise) - 1
            if 0 <= t_i < len(display_list):
                return display_list[t_i]
            else:
                print('Введите корректный номер трека')
        except ValueError:
            print('Введите номер или "m"')
            
def search_by_name():
    query = input('\nВведите название песни или исполнения: ').strip()
    if not query:
        print('Запрос не может быть пустым.')
        return ''
    params = {'name':  query}
    tracks = request_tracks(params)
    if tracks:
        selected_track = display_tracks_get_choiсe(tracks)
        handle_track(selected_track)

def select_by_mood():
    for key, (mood, tag) in MOOD_TAGS.items():
        print(f'{key}. {mood}')
    print('M - вернуться в главное меню')
    while True:    
        choise = input('Введите номер или m: ').strip().lower()
        if choise == 'm':
            return None  # сигнал о возврате в меню
        
        if choise in MOOD_TAGS:
            mood_name, tag = MOOD_TAGS[choise]
            params = {'tags': tag}
            tracks = request_tracks(params)
            if tracks:
                selected_track = display_tracks_get_choiсe(tracks)
                handle_track(selected_track)
            break
        else:
            print('введите число из списка')

def handle_track(track: dict):
    if track is None:
        return
    download_link = track.get('audiodownload')
    if download_link:
        print('Ссылка на трек: ')
        print(download_link)
    else:
        print('ссылка недоступна')
    print('Нажмите "Enter" для возрващения в главное меню')
    input(':')

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Выберите действие: ')
        print('1. Поиск по названию')
        print('2. Подборка по настроению')
        print('0. Выход')
        choise = input('Ваш выбор: ').strip()
        if choise == '1':
            search_by_name()
        elif choise == '2':
            select_by_mood()
        elif choise == '0':
            break
        else:
            print('Некорректный выбор. ')
            input('Нажмите "Enter" для продолжения')


main_menu()