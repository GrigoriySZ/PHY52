import sqlite3

DB_PATH = 'shop.db'

def create_table_products():
    """Создает таблицу products с продуктами в базе данных"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            create table if not exists products(
            id integer primary key autoincrement,
            name text not null,
            price real not null,
            quantity integer not null,
            is_available int default 1
            );
        ''')

        print('Products создана!')

def create_table_users():
    """Создает таблицу users с пользователями в базе данных"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            create table if not exists users(
            id integer primary key autoincrement,
            name text unique not null,  
            phone text not null
            );
        ''')
        print('Users создана!')

def create_table_orders():
    """Создает таблицу oreders с заказами в базе данных"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            create table if not exists orders(
            id integer primary key autoincrement,
            total_amount real not null,
            order_date text not null
            );
        ''')
        print('Orders создана!')

def create_table_order_details():
    """Создает таблицу order_details с деталями заказов в базе данных"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            create table if not exists order_details(
            id integer primary key autoincrement,
            order_id integer,
            product_id integer, 
            quantity integer not null, 
            foreign key (order_id) references orders(id),
            foreign key (product_id) references products(id)
            );
        ''')
        print('Order_details создана!')

def fill_products():
    """Добавляет записи в таблицу products"""

    data = [
        ('Ноутбуки', 50_000.0, 10), 
        ('Наушники', 5_900.0, 50),
        ('Монитор', 15_300.0, 35)
    ]

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany('''
            insert into products (name, price, quantity)
            values (?, ?, ?);
        ''', data)

        conn.commit()
        print('Products заполнена данными')

def fill_users():
    """Добавляет записи в таблицу users"""

    data = [
        ('Василий', '+89996552213'), 
        ('Ульяна', '85557774452'),
        ('Егор', '89235558879')
    ]

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany('''
            insert into users (name, phone)
            values (?, ?);
        ''', data)

        conn.commit()
        print('Users заполнена данными')

def fill_orders():
    """Добавляет записи в таблицу orders"""

    data = [
        (61_200.0, '2025-12-22'), 
        (36_500.0, '2025-03-13'),
        (11_800.0, '2025-05-26')
    ]

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany('''
            insert into orders (total_amount, order_date)
            values (?, ?);
        ''', data)

        conn.commit()
        print('Orders заполнена данными')

def fill_order_details():
    """Добавляет записи в таблицу order_details"""

    data = [
        (1, 1, 1), 
        (1, 2, 1),
        (1, 3, 1),
        (2, 3, 2),
        (2, 2, 1),
        (3, 2, 2)
    ]

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany('''
            insert into order_details (order_id, product_id, quantity)
            values (?, ?, ?);
        ''', data)

        conn.commit()
        print('Order_details заполнена данными')

def alter_table_orders():
    """Дополняет таблицу orders"""

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            alter table orders add column 
            user_id integer references users(id);
        ''')

        conn.execute('''
            update orders set user_id = 1
            where id = 1;
        ''')

        conn.execute('''
            update orders set user_id = 3
            where id = 2;
        ''')

        conn.execute('''
            update orders set user_id = 2
            where id = 3;
        ''')

        print('Orders таблица обновлена')

def agregation_func():
    """ """

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            select sum(quantity), avg(price)
            from products;
        ''')

        total_stock, avg_price = cursor.fetchone()

        print(f'Общее количество: {total_stock} шт.')
        print(f'Средняя цена товара: {avg_price} руб.')

        cursor.execute('''
            select max(price) from products;
        ''')

        max_price = cursor.fetchone()

        print(f'Максимальная цена: {max_price} руб.')


if __name__ == '__main__':

    # Создаём таблицы в базе данных
    create_table_products()
    create_table_users()
    create_table_orders()
    create_table_order_details()

    # Заполняем таблицы данными
    # fill_products()
    # fill_users()
    # fill_orders()
    # fill_order_details()

    # Дополняем таблицу orders
    # alter_table_orders()

    # primary key - первичный ключ
    # foreign key - внешний ключ 
    # (содержит значения первичных ключей, связанной с ней таблиц)

    # Агрегирующие функции (возвращает скалярное(одно) значение)
    # COUNT() - считает количество записей в таблице или столбце
    # SUM() - считает сумму значений в столбце
    # AVG() - считает средние значение в столбце
    # MIN()/MAX() - Выводит минимальное или максимальное значение по столбцу

    # SELECT column, [функция агрегации] FROM table 
    # WHERE condition 
    # 
    # Пример написания функции агрегации
    # select COUNT(user_id) as count_user from orders -> count_user = 1

    # SQL Academy - тренажер по задачами по языку SQL