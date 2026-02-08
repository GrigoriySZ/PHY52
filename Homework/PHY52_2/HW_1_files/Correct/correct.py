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
            return None   # добавила return в этой ветке
    return wrapper

@file_is_exist #добавила декоратор так как идет работа с файлом
def word_count(filename: str, exclude_stop_words: bool = False):
    """Считает и возвращает общее количество слов в файле."""
    words = read_all_words(filename, exclude_stop_words)
    return len(words)



@file_is_exist  #снова декоратор
def find_word(filename: str, target_word: str, exclude_stop_words: bool = False):
    """Ищет слово 'target' в файле и возвращает количество упоминаний"""
    if not target_word or not isinstance(target_word, str):
        print("Ошибка: указано пустое или некорректное слово для поиска")
        return 0
    
    target_word = target_word.lower()
    words = read_all_words(filename, exclude_stop_words)
    
    #ищем точные совпадения
    count = sum(1 for word in words if word == target_word)
    return count


def top_words(filename: str, top_n: int = 5, exclude_stop_words: bool = False):
    """Возвращает топ-N самых частых слов"""
    word_freq = get_word_frequency(filename, exclude_stop_words)
    top_words_list = Counter(word_freq).most_common(top_n)
    return top_words_list


@file_is_exist  #
def save_statistics(filename: str, top_n: int = 5, exclude_stop_words: bool = False):
    """Сохраняет статистику в файл stats.txt"""
    try:
        total_words = word_count(filename, exclude_stop_words)
        top_words_list = top_words(filename, top_n, exclude_stop_words)
        
        with open("stats.txt", "w", encoding="UTF-8") as file:
            file.write(f"Общее количество слов в файле '{filename}' - {total_words}\n")
            file.write(f"Top-{top_n} самых употребляемых слов в файле '{filename}':\n")
            
            for i, (word, count) in enumerate(top_words_list, 1):
                file.write(f"\t{i}) {word.capitalize()}: {count}\n")
        
        print(f"Статистика сохранена в файл stats.txt")
        
    except Exception as e:
        print(f"Ошибка при сохранении статистики: {e}")

def clear_line(line: str):
    """Убирает пунктуационные знаки из строки"""
    for key in PUNCTUATION:
        line = line.replace(key, " ")
    #заменяем двойные пробелы на одинарные
    while "  " in line:
        line = line.replace("  ", " ")
    return line.strip().lower()


@file_is_exist
def read_all_words(filename: str, exclude_stop_words: bool = False):
    """Читает все слова из файла"""
    words = []
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                cleaned_line = clear_line(line)
                if cleaned_line:
                    line_words = cleaned_line.split()
                    if exclude_stop_words:
                        line_words = [w for w in line_words if w not in EXCEPTION_WORDS]
                    words.extend(line_words)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []
    return words




def get_word_frequency(filename: str, exclude_stop_words: bool = False):
    """Возвращает частотный словарь слов"""
    words = read_all_words(filename, exclude_stop_words)
    return dict(Counter(words))






word = "Кролик-программист"
try:
    print(f"Слово {word} упоминается в {PATH} - {find_word(PATH, word)}"
          f" {"раза" if find_word(PATH, word) % 10 in (2, 3, 4) else "раз"}.")
except TypeError:
    print("Error")
except KeyError:
    print("Ошибка! Остуствует слове для поиска")
save_statistics(PATH, 7, True)


TEACHER_NOTES = """
в find_word если слово не найдено, вызов words_in_file(filename)[target.lower()] вызовет KeyError
у вас в коде есть try/except TypeError, но это не ловит KeyError
функции word_count и words_in_file обе читают файл построчно, хотя можно было бы переиспользовать логику. """