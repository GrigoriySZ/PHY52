import os
from functools import wraps
from collections import Counter


PATH = "book.txt"
EXCEPTION_WORDS = ("и", "в", "на", "c")
PUNCTUATION = (".", ",", "!", "'", "\"", "_", "—", "\n", ":", ";")


def file_is_exist(func):
    """Проверяет наличие файла по заданному пути"""
    @wraps(func)
    def wrapper(filename: str, *args, **kwargs):
        if os.path.exists(filename):
            return func(filename, *args, **kwargs)
        else:
            print(f"Файл {filename} не найден!")
    return wrapper


@file_is_exist
def word_count(filename: str, exception: bool=False):
    """Считает и возвращает общее количество слов в файле.
    Если exception=True - не считаем слова исключения. По умолчанию exception=False."""
    words = get_all_words(filename, exception)
    return len(words)

@file_is_exist
def words_in_file(filename: str, exception: bool=False):
    """Создает словарь всех слов в файле 'filename' с количеством их употреблений.
    Если exception=True - не учитываем слова исключения. По умолчанию exception=False."""
    words = get_all_words(filename, exception)
    words_dict = {}
    for w in words:
        words_dict[w] = words_dict.get(w, 0) + 1
    return words_dict

@file_is_exist
def find_word(filename: str, target: str):
    """Ищет слово 'target' в файле и возвращает общее количество упоминаний 'target' в файле"""
    words_dict = words_in_file(filename)
    target_lower = target.lower()
    return words_dict.get(target_lower, 0)



def top_words(filename: str, top: int=5, exception: bool=False):
    """Создает список из наиболее часто используемых слов.
    - top - задается количество самых употребляемых слов. По умолчанию top=5.
    - exception - при True не учитывает слова исключения. По умолчанию exception=False."""
    top_words_list = Counter(words_in_file(filename, exception)).most_common(top)
    return top_words_list



def save_statistic(filename: str, top: int=5, exception: bool=False):
    """Сохраняет статистику в файл stats.txt.
    - top - задается количество самых употребляемых слов. По умолчанию top=5.
    - exception - при True не учитывает слова исключения. По умолчанию exception=False."""
    i = 0
    with open("stats.txt", "w", encoding="UTF-8") as file:
        file.write(f"Общее количество слов в файле '{filename}' - {word_count(filename, exception)}\n")
        file.write(f"Top-{top} самых употребляемых слов в файле '{filename}':\n")
        for w in top_words(filename, top, exception):
            i += 1
            file.write(f"\t{i}) {str(w[0]).capitalize()}: {w[1]}\n")


def clear_line(line: str):
    """Убирает пунктуационные знаки из строки"""
    for key in PUNCTUATION:
        line = line.replace(key, "")
    clean_line = line.replace("-", " ").lower()
    return clean_line

def line_to_list(line: str):
    """Переводит строку в список слов"""
    converted_line = clear_line(line)
    return converted_line.strip().split()

def get_all_words(filename: str, exception: bool = False):
    """Функция для получения всех слов из файла.
    Возвращает список всех слов (с учетом параметра exception)."""
    words = []
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            striped_line = line_to_list(line)
            for w in striped_line:
                if exception and w in EXCEPTION_WORDS:
                    continue
                words.append(w)
    return words




word = "Кролик"
try:
    count = find_word(PATH, word)
    print(f"Слово {word} упоминается в {PATH} - {count} "
          f"{'раза' if count % 10 in (2, 3, 4) and count % 100 not in (12, 13, 14) else 'раз'}.")
except TypeError:
    print("Error")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
save_statistic(PATH, 7, True)