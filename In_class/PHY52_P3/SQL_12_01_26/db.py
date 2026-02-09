import sqlite3  # Библиотека для запросов к БД

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('''
create table if not exists users(
               id integer primary key autoincrement,
               name text unique,  
               phone text not null,
               is_admin integer default 0);
''')

# autoincrement - автоматическое преращиение значение при создании
# primary key - одновременно объединяет уникальность и обязательность значения. Обязателен для ID
# unique - ограничение уникальности
# not null - ограничение 

name = input('name: ')
phone = input('phone: ')

cursor.execute('''
    insert into users(name, phone)
    values (?, ?) ;
''', (name, phone))  # Добавляем данные в БД с подстановкой атрибутов

conn.commit()  # Сохраняем и подтверждаем наши дейсвтия в БД 

cursor.execute('select * from users')  # Запрос всех данных из БД

# row = cursor.fetchone()  # Запрос одного значения (одной строки)
rows = cursor.fetchall()  # Запрост всех значений (всех строк)

print(rows)

cursor.close()  # Закрытие пространстра управления
conn.close()  # Отключение от базы данных