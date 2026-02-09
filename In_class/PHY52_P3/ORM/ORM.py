# pip install SQLAlchemy
# ORM - объектно ориентированная модель

# Миграция - версионирование базы данных

import sqlalchemy  # Библиотека ORM 
from typing import Optional
from sqlalchemy import Engine, String, Integer, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship


# engine - для взаимодействия с базой данных 
# Base()
# Mapped - приведение типов данных под тип данных базы данных
# Mapped[int] = INTEGER
# Mapped[str] = TEXT
# mapped_column - функция для создания колонки 

# Создание таблиц в БД SQLite с помощью SQLAlchemy 

# Подключаемся к движку. echo=True - будет показывать SQL запросов
engine = sqlalchemy.create_engine('sqlite:///example.db', echo=True)

# Создаем базовый класс для модели и наследуем от DeclarativeBase.

class Base(DeclarativeBase):
    pass

# Модель - это класс ORM. Модели называем в единственном числа

# Последующие классы наследует уже от базового класса Base
class User(Base):
    # Задаем название таблицы
    __tablename__ = 'users' # Название таблицы в базе данных. Называем во мн.ч.

    # Задаем название колонок (полей) таблицы
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)  # 30 - ограничение по длине
    age: Mapped[int] = mapped_column(Integer)
    fullname: Mapped[Optional[str]] # optional - может быть Null

    # Создаем связь с моделью Post через relationship
    posts: Mapped[list['Post']] = relationship(back_populates='author')

# One-to-Many (Foreign key в дочерней таблице + relationship() в обеих таблицах)
# Many-to-Many (Промежуточная таблица)

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    
    # Обращение к атрибуту происходит через имя таблицы
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    # Обращение к User через название модели
    author: Mapped['User'] = relationship(back_populates='posts')
    # User - модель, автор - атрибут связи, posts - атрибут связи в User


# Основные методы для работы с моделью:
# Все методы выполняем через сессии

# session.add(obj) - Подготавливает объект к сохранению (INSERT)
# session.commit() - Сохраняет изменения в БД
# session.scalar() - Получение одну запись (строку) из БД 
# session.scalars() - получает список всех записей 

# Создаст таблицы на основе модели, наследованных от Base
Base.metadata.create_all(engine)  

# Пример создания сессии
with Session(engine) as session:
    
    # Объявляем новый объект User
    new_user = User(name='Ivan', age=10, fullname='Ivan Ivanov')

    # Добавляем данные в базу данных
    session.add(new_user)

    # Сохраняем добавленные данные
    session.commit()

    # Создаем запрос к базе данных в c фильтрацией по имени
    query = select(User).where(User.name=='Ivan')

    # Передаем запрос к базе данных
    user = session.scalar(query)

    print(f'Пользователь: {user.fullname}')