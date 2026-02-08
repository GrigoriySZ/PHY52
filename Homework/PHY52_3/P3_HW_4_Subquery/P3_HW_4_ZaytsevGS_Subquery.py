import sqlite3

DB_PATH = 'library.db'


def create_tables(db_path: str):
    """ Создает таблицы в базе данных:
        authors   (author_id, name, country)
        genres    (genre_id, name)
        books     (book_id, title, author_id, genre_id, published_year, price, quantity)
        clients   (client_id, first_name, last_name, email)
        orders    (order_id, client_id, book_id, order_date, quantity, status)
    
    """

    with sqlite3.connect(db_path) as conn:

        conn.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL CHECK (name <> ''),
                country TEXT
            );
        ''')

        print('Таблица authors создана в базе данных.')

        conn.execute('''
            CREATE TABLE IF NOT EXISTS genres (
                genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name NEXT NOT NULL UNIQUE
            );
        ''')

        print('Таблица genres создана в базе данных.')
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title NEXT NOT NULL CHECK (title <> ''),
                author_id INTEGER NOT NULL,
                genre_id INTEGER NOT NULL,
                published_year INTEGER CHECK (published_year >= 0),
                price REAL NOT NULL CHECK (price >= 0.0),
                quantity INTEGER NOT NULL CHECK (quantity >= 0) DEFAULT 0,
                FOREIGN KEY (author_id) REFERENCES authors(author_id),
                FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
            );
        ''')

        print('Таблица books создана в базе данных.')

        conn.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name NEXT NOT NULL CHECK (first_name <> ''),
                last_name NEXT NOT NULL CHECK (last_name <> ''),
                email TEXT UNIQUE
            );
        ''')

        print('Таблица clients создана в базе данных.')

        conn.execute(f'''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                order_date TEXT NOR NULL DEFAULT (DATE('now')),
                quantity INTEGER NOT NULL CHECK (quantity > 0),
                status TEXT NOT NULL DEFAULT 'В обработке'
                CHECK (status IN ('В обработке', 'Выполнен', 'Отменен')),
                FOREIGN KEY (client_id) REFERENCES clients(client_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            );
        ''')

        print('Таблица orders создана в базе данных.')

def fill_tables(db_path: str):
    """Добавляет данные в базу данных.

    Таблицы в базе данных:
        authors   (author_id, name, country)
        genres    (genre_id, name)
        books     (book_id, title, author_id, genre_id, published_year, price, quantity)
        clients   (client_id, first_name, last_name, email)
        orders    (order_id, client_id, book_id, order_date, quantity, status)
    
    """
    with sqlite3.connect(db_path) as conn: 

        conn.execute('''
            INSERT INTO authors (name, country) VALUES
            ('Ф.М. Достоевский', 'Россия'),
            ('Дж. Роулинг', 'Великобритания'),
            ('Дж. Оруэлл', 'Великобритания'),
            ('Рэй Брэдбери', 'США'),
            ('Эрих Мария Ремарк', 'Германия');
        ''')

        print('В таблицу authors добавлены записи.')

        conn.execute('''
            INSERT INTO genres (name) VALUES
            ('Роман'),
            ('Фэнтези'),
            ('Антиутопия'),
            ('Научная фантастика'),
            ('Классика');
        ''')

        print('В таблицу genres добавлены записи.')

        conn.execute('''
            INSERT INTO books (
            title, author_id, genre_id, 
            published_year, price, quantity
            ) VALUES
            ('1984', 3, 3, 1949, 379.0 ,38),
            ('Гарри Поттер и философский камень', 2, 2, 1997, 1149.0, 18),
            ('Идиот', 1, 1, 1869, 749.0, 15),
            ('Три товарища', 5, 5, 1936, 449.0, 25),
            ('451 градус по Фаренгейту', 4, 4, 1953, 649.0, 31);
        ''')

        print('В таблицу books добавлены записи.')

        conn.execute('''
            INSERT INTO clients (first_name, last_name, email) VALUES
            ('Ксения', 'Антипова', 'antipova_ksenia_v@gmail.com'),
            ('Павел', 'Бачин', 'bachin.pavel@mail.ru'),
            ('Эдуард', 'Воронков', 'e-b-voronkin@yahoo'),
            ('Галина', 'Лузина', 'LusinaGK@ya.ru'),
            ('Андрей', 'Перцевой', 'anton_papper@yahoo.org'),
            ('Анна', 'Сударева', 'SidatAA@gmail.com');
        ''')

        print('В таблицу clients добавлены записи.')

        conn.execute('''
            INSERT INTO orders (
            client_id, book_id, order_date, quantity, status
            ) VALUES 
            ( 3, 1, '2024-10-15', 1, 'Выполнен'),
            ( 1, 2, '2025-06-10', 1, 'Выполнен'),
            ( 1, 5, '2021-07-13', 3, 'Отменен'),
            ( 2, 4, '2026-01-20', 1, 'В обработке'),
            ( 2, 1, '2025-05-22', 1, 'Выполнен'),
            ( 4, 2, '2024-01-10', 2, 'Отменен'),
            ( 4, 2, '2024-01-10', 1, 'Выполнен'),
            ( 5, 1, '2026-01-30', 3, 'Выполнен'),
            ( 2, 4, '2025-12-30', 1, 'В обработке');
        ''')

        print('В таблицу orders добавлены записи.')

def show_books_and_year(db_path: str):  # Простой SELECT
    """Выводит название всех книг и год издания"""

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT title, published_year 
            FROM books
            ORDER BY published_year DESC;
        ''')
        
        books_list = cursor.fetchall()

        print('Список всех книг и год издания:')
        if books_list:
            for index, (title, published_year) in enumerate(books_list, 1):
                print(f'{index:3}. Книга: "{title}". Издание: {published_year} г.')
        else:
            print(f'{'':3} Список книг пуст!')

def show_books_and_author(db_path: str):  # SELECT c JOIN (один)
    """Выводит название всех книг и имя автора"""

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT b.title, a.name
            FROM books b
            JOIN authors a
            ON b.author_id = a.author_id;
        ''')

        books_list = cursor.fetchall()

        print('Список всех книг и имя автора:')
        if books_list:
            for index, (title, author_name) in enumerate(books_list, 1):
                print(f'{index:3}. Книга: "{title}". Автор: {author_name}')
        else:
            print(f'{'':3} Список книг пуст!')

def show_customers_books(db_path: str): # SELECT с JOIN (несколько)
    """Выводит имена клиентов и название книг, 
    которые они заказывали в январе 2024 года.
    Сортировка по имени клиента
    
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT c.first_name, b.title, 
            strftime ("%d.%m.%Y", o.order_date), 
            o.status 
            FROM clients c
            JOIN orders o
            ON c.client_id = o.client_id
            JOIN books b
            ON o.book_id = b.book_id
            WHERE o.order_date BETWEEN '2024-01-01' AND '2024-01-31'
            ORDER BY c.first_name;
        ''')

        clients_list = cursor.fetchall()

        print('Список клиентов с заказом в январе 2024 г.:')
        if clients_list:
            for index, (client_name, book_title, 
                        order_date, order_status
                        ) in enumerate(clients_list, 1):
                print(f'{index:2}. Клиент: {client_name.title()}')
                print(f'{'':4}L Книга: "{book_title}"')
                print(f'{'':4}L Дата заказа: {order_date} г.')
                print(f'{'':4}L Статус: "{order_status}".')
        else: 
            print(f'{' ':3} Заказов в январе не было.')

def count_books(db_path: str):  # GROUP BY(?) и агрегирующая функция
    """Вычисляет общее количество книг на складе"""
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT SUM(b.quantity) AS total_books
            FROM books b;
        ''')

        total_books, *_ = cursor.fetchone()

        print(f' - Общее количество книг на складе: {total_books} шт.')

def show_expensive_genres(db_path: str):  # GROUP BY + HAVING
    """Выводит жанры, у которых средняя цена книг выше 500 рублей"""
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT g.name, AVG(b.price) as avg_price
            FROM genres g
            JOIN books b
            ON g.genre_id = b.genre_id
            GROUP BY g.name
            HAVING avg_price > 500.0
            ORDER BY avg_price DESC;
        ''')

        avg_genre_prices_list = cursor.fetchall()

        print('Список жанров со средней ценой больше 500 рублей:')
        if avg_genre_prices_list:
            for index, (genre, avg_price) in enumerate(avg_genre_prices_list, 1):
                print(f'{index:2}. - Жанр: "{genre}"')
                print(f'    L Средняя цена товаров в жанре: {avg_price:.2f} руб.')
        else:
            print(' - Среди жанров нет среднего ценника больше 500 руб.')

def show_unsold_books(db_path: str):  # Subquery
    """Выводит название книг, которые никогда не заказывались"""

    with sqlite3.connect(db_path) as conn: 
        cursor = conn.cursor()

        cursor.execute('''
            SELECT title 
            FROM books
            WHERE book_id NOT IN 
                (SELECT book_id FROM orders)
        ''')

        unsold_books_list = cursor.fetchall()

        print('Список книг, которые никогда не заказывали:')
        if unsold_books_list:
            for index, (title,) in enumerate(unsold_books_list, 1):
                print(f'{index:2}. "{title}"')
        else:
            print(' - В списке нет ни одной книги без заказов.')

def show_orders_for_month(db_path: str):  # date('now')
    """Выводит список заказов за последние 30 дней"""

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT o.order_id, strftime ('%d.%m.%Y', o.order_date), 
            o.status, o.quantity,
            c.first_name, c.last_name, b.title
            FROM orders o
            JOIN clients c
            ON o.client_id = c.client_id
            JOIN books b 
            ON o.book_id = b.book_id
            WHERE o.order_date >= DATE('now', '-30 days');
        ''')

        orders_for_month_list = cursor.fetchall()

        if orders_for_month_list:
            for index, (id, date, status, quantity,
                        f_name, l_name, title, 
                        ) in enumerate(orders_for_month_list, 1):
                
                print(f'{index:2}. Номер заказа: {id}; Дата: {date} г.; Статус: {status}.')
                print(f'{'':4}L Клиент: {f_name.title()} {l_name.title()}')
                print(f'{'':4}L Товар: "{title}". Количество: {quantity} шт.')

def increase_fantasy_price(db_path: str):
    """Увеличивает цену всех книг в жанре 'Фэнтези' на 10%."""

    with sqlite3.connect(db_path) as conn:

        conn.execute('''
            UPDATE books AS b
            SET price = price * 1.1
            WHERE EXISTS (
                SELECT 1
                FROM genres g
                WHERE b.genre_id = g.genre_id
                AND g.name = 'Фэнтези'
                );
        ''')

        conn.commit()

def delete_inactive_customers(db_pah: str):
    """Удаляет клиентов, которые не сделали ни одного заказа"""

    with sqlite3.connect(db_pah) as conn:
        cursor = conn.cursor()

        cursor.execute('''
        SELECT client_id, first_name, last_name, email
        FROM clients
        ''')
        old_clients_list = cursor.fetchall()

        print('Удаление клиентов без заказов...')
        conn.execute('''
            DELETE FROM clients AS c
            WHERE c.client_id NOT IN (
                SELECT client_id
                FROM orders o
                WHERE c.client_id = o.client_id
                );
        ''')

        cursor.execute('''
            SELECT client_id, first_name, last_name, email
            FROM clients
        ''')
        new_clients_list = cursor.fetchall()

        deleted_clients_list = [client for client in old_clients_list
                                if client not in new_clients_list]

        if deleted_clients_list:
            print('Клиенты без заказов успешно удалены из базы.')

            print('Список удалённых клиентов:')
            for index, (client_id, first_name,
                        last_name, email
                        ) in enumerate(deleted_clients_list, 1):
                print(f'{index:2}. "{client_id}": {first_name} {last_name}')
                print(f'{'':3} L email: {email}')
        else:
            print('В базе нет клиентов без заказов.')

        conn.commit()

def show_authors_stats(db_path: str):
    """Подсчитывает и выводит общее количество проданных книг
    для каждого автора в базе с пометкой заказа 'Выполнен'.

    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT a.name, SUM(o.quantity) AS total_sold
            FROM authors a
            JOIN books b
            ON a.author_id = b.author_id
            JOIN orders o
            ON b.book_id = o.book_id
            WHERE o.status = 'Выполнен'
            GROUP BY a.name
            ORDER BY total_sold DESC;
        ''')

    authors_stats_list = cursor.fetchall()

    if authors_stats_list:
        print('Список общих продаж автора:')
        for index, (name, total_sold) in enumerate(authors_stats_list, 1):
            print(f'{index:2}. Автор: {name}')
            print(f'{'':3} L Общие продажи автора: {total_sold} шт.')
    else:
        print('В базе нет ни одной проданной книги.')

if __name__ == '__main__':
    
    # create_tables(DB_PATH)
    # fill_tables(DB_PATH)
    show_books_and_year(DB_PATH)
    show_books_and_author(DB_PATH)
    show_customers_books(DB_PATH)
    count_books(DB_PATH)
    show_expensive_genres(DB_PATH)
    show_unsold_books(DB_PATH)
    show_orders_for_month(DB_PATH)
    increase_fantasy_price(DB_PATH)
    delete_inactive_customers(DB_PATH)
    show_authors_stats(DB_PATH)