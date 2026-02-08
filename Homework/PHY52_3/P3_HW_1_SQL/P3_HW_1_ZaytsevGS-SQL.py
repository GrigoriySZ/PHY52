import sqlite3

DB_PATH = 'BookStore.db'

def create_authors_table():
    """Создает таблицу Authors в базе данных BookStore.db"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE table if not exists authors(
            author_id integer primary key autoincrement,
            first_name text not null,
            last_name text not null
            );
        ''')

        print('Таблица Authors создана!')

def create_books_table():
    """Создает таблицу Books в базе данных BookStore.db"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE table if not exists books(
            book_id integer primary key autoincrement,
            title text not null,
            author_id integer,
            price real not null,
            foreign key(author_id) references authors(id)
            );
        ''')

        print('Таблица Books создана!')

def fill_authors_table():
    """Добавляет записи в таблицу Authors"""

    data = [
        ('Джон', 'Толкин'),
        ('Лев', 'Толстой'),
        ('Джоан', 'Роулинг')
    ]

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany('''
            INSERT INTO authors(first_name, last_name)
            VALUES (?, ?);
        ''', data)

        # Сохраняем изменения
        conn.commit()
        print(f'В таблицу Authors добавлены записи: {len(data)} шт.')

def fill_books_table():
    """Добавляет записи в таблицу Books"""

    data = [
        ('Властелин колец. Хранители кольца', 1, 1_399.0),
        ('Война и мир. Том 1-2', 2, 799.0),
        ('Гарри Поттер и Философский камень', 3, 1_149.0)
    ]

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany('''
            INSERT INTO books(title, author_id, price)
            VALUES (?, ?, ?);
        ''', data)

        # Сохраняем изменения
        conn.commit()
        print(f'В таблицу Books добавлены записи: {len(data)} шт.')

def delete_data_in_authors_table():
    """Удаляет все записи из таблицы Authors"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''DELETE FROM authors;''')

        # Сохраняем изменения
        conn.commit()
        print('Таблица Authors очищена!')

def delete_data_in_books_table():
    """Удаляет все записи из таблицы Books"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''DELETE FROM books;''')

        # Сохраняем изменения
        conn.commit()
        print('Таблица Books очищена!')


if __name__ == '__main__':

    # Добавляем таблицы Authors и Books
    create_authors_table()
    create_books_table()

    # Добавляем в таблицы Authors и Books записи
    fill_authors_table()
    fill_books_table()

    # Удаляем из таблиц Authors и Books все значения
    delete_data_in_authors_table()
    delete_data_in_books_table()