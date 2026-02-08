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
            return None
    return wrapper

@file_is_exist
def word_count(filename: str, exception: bool=False):
    """Считает и возвращает общее количество слов в файле.
    Если exception=True - не считаем слова исключения. По умолчанию exception=False."""
    count = 0
    exception_count = 0
    while True:
        w = get_word(filename)
        if w in EXCEPTION_WORDS:
            exception_count += 1
        count += 1
        if exception:
            return count - exception_count
        else:
            return count

@file_is_exist
def words_in_file(filename: str, exception: bool=False):
    """Создает список всех слов в файле 'filename'.
    Если exceptiom=True - не учитываем слова исключения. По умолчанию exception=False."""
    words_dict = dict()
    while True:
        w = get_word(filename)
        if w in words_dict:
            words_dict[w] += 1
        else:
            words_dict[w] = 1
        if exception:
            words_dict_exc = {w: c for w, c in words_dict.items() if w not in EXCEPTION_WORDS}
            return words_dict_exc
        else:
            return words_dict

def find_word(filename: str, target: str):
    """Ищет слово 'target' в файле и возвращает общее количество упоминаний 'target' в файле"""
    try:
        if target:
            count_word = words_in_file(filename)[target.lower()]
            return count_word
        else:
            raise KeyError
    except KeyError:
        print("Ошбика ввода! Введите искомое слово")

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
    else:
        clean_line = line.replace("-", " ").lower()
    return clean_line

def line_to_list(line: str):
    """Переводит строку в список слов"""
    converted_line = clear_line(line)
    return converted_line.strip().split()

def get_word(filename: str):
    """Выдает слово по одному"""
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            striped_line = line_to_list(line)
            for w in striped_line:
                return w
        else:
            return False


word = ""
try:
    print(f"Слово {word} упоминается в {PATH} - {find_word(PATH, word)}"
          f" {"раза" if find_word(PATH, word) % 10 in (2, 3, 4) else "раз"}.")
except TypeError:
    print("Error")
except KeyError:
    print("Ошибка! Остуствует слове для поиска")
save_statistic(PATH, 7, True)


TEACHER_NOTES = """
в find_word если слово не найдено, вызов words_in_file(filename)[target.lower()] вызовет KeyError
у вас в коде есть try/except TypeError, но это не ловит KeyError
функции word_count и words_in_file обе читают файл построчно, хотя можно было бы переиспользовать логику. """