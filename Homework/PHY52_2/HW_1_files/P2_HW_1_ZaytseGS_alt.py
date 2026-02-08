import os
from functools import wraps
from collections import Counter
from logging import exception

PATH = 'book.txt'
EXCEPTION_WORDS = ('и', 'в', 'на', 'c')
PUNCTUATION = ('.', ',', '!', '"', '\'', '_', '—', '\n', ':', ';')


def file_is_exist(func):
    """Проверяет наличие файла по заданному пути"""
    @wraps(func)
    def wrapper(filename: str, *args, **kwargs):
        if os.path.exists(filename):
            return func(filename, *args, **kwargs)
        else:
            print(f'Файл {filename} не найден!')
            return None
    return wrapper

def __read_file(filename: str):
    """Читает файл 'filename' и выдает построчно"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
                yield line.strip()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def __clear_and_separate_line(line: str):
    """Отчищает строку от пунктуационных знаков и разделяет на отдельные слова"""
    for key in PUNCTUATION:
        line = line.replace(key, '')
    else:
        line = line.replace('-', ' ')
    clear_line = line.strip().split()
    print(clear_line)
    return clear_line

@file_is_exist
def word_count(filename: str, exclude_stopwords: bool = False):
    """Считает и возвращает общее количество слов в файле.
    Если exclude_stopwords=True - не считает слова исключения.
    По умолчанию exclude_stopwords=False"""
    count = 0
    exc_count = 0
    for line in __read_file(filename):
        for word in __clear_and_separate_line(line):
            if word in EXCEPTION_WORDS:
                exc_count += 1
            count += 1
    return count - exc_count if exclude_stopwords else count

def get_all_words(filename: str, exclude_stopwords: bool = False):
    """Создает и выдает словарь со всеми словами из текста"""
    words_dict = dict()
    for line in __read_file(filename):
        for word in __clear_and_separate_line(line):
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    if exclude_stopwords:
        words_without_stopwords = [word for word in words_dict if word not in EXCEPTION_WORDS]
        return words_without_stopwords
    else:
        return words_dict



