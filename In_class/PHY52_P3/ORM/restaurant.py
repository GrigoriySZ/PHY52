from sqlalchemy import (ForeignKey, Table, Column,
                        String, Float, Integer,
                        create_engine, select, 
                        not_, func)

from sqlalchemy.orm import (Session, DeclarativeBase, Mapped, 
                            mapped_column, relationship)

from sqlalchemy.exc import NoResultFound


engine = create_engine('sqlite:///restaurant.db', echo=True)


class Base(DeclarativeBase):
    pass


order_items = Table(
    'order_items',  # Название ассоциативной таблицы
    Base.metadata, 
    Column('order_id', ForeignKey('orders.id'), primary_key=True),
    Column('dishes_id', ForeignKey('dishes.id'), primary_key=True)
)

class RestTable(Base):
    __tablename__ = 'tables'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    capacity: Mapped[int]
    is_available: Mapped[bool] = mapped_column(nullable=False)
    orders: Mapped[list['Order']] = relationship(back_populates='tables')

class Dish(Base):
    __tablename__ = 'dishes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    calories: Mapped[float] = mapped_column(default=0)
    price: Mapped[float]
    orders: Mapped[list['Order']] = relationship(back_populates='dishes', secondary=order_items)
    # back_populates - название атрибута
    # secondary - объект таблицы посредника

class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(default='принят')
    table_id: Mapped[int] = mapped_column(ForeignKey('tables.id'))
    table: Mapped['RestTable'] = relationship(back_populates='orders')
    dishes: Mapped[list['Dish']] = relationship(back_populates='orders', secondary=order_items)

    @property
    def total_price(self) -> float:
        # dishes_prices = []
        # for dish in self.dishes:
        #     dishes_prices.append(dish_price)
        # return sum(dishes_prices)
        return sum(dish.price for dish in self.dishes)

Base.metadata.create_all(engine)

def get_free_tables(session: Session):

    # Ищем столы со статусом заказа 'Принято'
    query = select(Order.table_id).where(Order.status == 'принят')

    # Отсортировываем столы с принятыми заказами
    query2 = select(RestTable).where(not_(RestTable.id.in_(query)))

    # Возвращаем список
    return session.scalars(query2).all()

def get_popular_dish(session: Session):
    
    query = (select(Dish.name, 
                   func.count(order_items.c.order_id).label('total_sales'))
                   .join(order_items)
                   .group_by(Dish.id)
                   .order_by(func.count(order_items.c.order_id).desc()))
    
    # session.execure() вернет список кортежей
    return session.execute(query).all()

def get_dish(session: Session, order_id: int, dish_name: str):
    try:
        # 1. Пытаемся найти блюдо
        query = select(Dish).where(Dish.name==dish_name)
        
        # session.scalar_one() Выбросит исключение, если ничего не найдет
        dish = session.execute(query).scalar_one()

        # 2. Пытаемся найти заказ
        order = session.get(Order, order_id)
        if not order:
            print('Заказ не найден')
            return
        
        # Добавляем блюдо в заказ
        order.dishes.append(dish)
        session.commit()
        print(f'Блюдо {dish_name} добавлено в заказ.')
    except NoResultFound:
        print(f'Ошибка: Блюда {dish_name} не найдено.')
    except Exception as e:
        session.rollback()
        print(f'Произошла непредвиденная ошибка: {e}')

# МИГРАЦИЯ БАЗ ДАННЫХ
# Библиотека для миграций
# pip install alembic
# alembic init migrations - создание файлов миграции
# alembic revision --autogenerate -m "add calories in dish" - создание файла миграции
# alembic revision --autogenerate -m "add is_available in resttable" 
# alembic upgrade head
# alembic revision --autoupgrade -m "add nullable true in calories"

if __name__ == '__main__':
    """
    with Session(engine) as session:

        # Создаем записи для добавления в таблицу tables
        table1 = RestTable(number=1, capacity=2)
        table2 = RestTable(number=2, capacity=4)
        
        # Создаем записи для добавления в таблицу orders
        pizza = Dish(name='Маргарита', price=690.0)
        pasta = Dish(name='Карбонара', price=460.0)
        coffee = Dish(name='Капучино', price=280.0)

        sandwich = Dish(name='Сэндвич-клаб', price=380.0)
        cake = Dish(name='Медовик', price=410.0)
        tea = Dish(name='Облепиховый чай', price=210.0)
        
        # Добавляем данные в заказ 1
        order1 = Order(table=table1)
        order1.dishes.append(pizza)
        order1.dishes.append(pasta)
        order1.dishes.append(coffee)

        # Добавляем данные в заказ 2
        order2 = Order(table=table2)
        order2.dishes.append(tea)
        order2.dishes.append(sandwich)
        order2.dishes.append(cake)

        # Добавляем все данные в базу данных
        session.add_all([table1, table2, 
                        pizza, pasta, coffee, 
                        tea, sandwich, cake, 
                        order1, order2])

        # Сохраняет данные в базу данных
        session.commit()
        print('Данные добавлены')

    with Session(engine) as session:

        query = select(Order).where(Order.id==1)
        my_order = session.scalar(query)
        print(f'Сумма заказа: {my_order.id}: {my_order.total_price} руб.')

    with Session(engine) as session:

        tables = get_free_tables(session)
        if tables:
            print(f'Количество свободных столов: {len(tables)}')
            for t in tables:
                print(f'#{t.number}. Вместимость: {t.capacity}')
        else:
            print('Столики не найдены.')       

    with Session(engine) as session:

        dishes = get_popular_dish(session)
        print(dishes)
        max_count = dishes[0][1]  # количество максимальное
        for row in dishes:
            dish_name = row.name
            sales_count = row.total_sales
            if sales_count == max_count:
                print(dish_name)

    with Session(engine) as session:
        get_dish(session, 1, 'Медовик')
    """
    
    