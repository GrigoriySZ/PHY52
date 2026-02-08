from sqlalchemy import (ForeignKey, Table, Column,
                        String, Float, Integer,
                        CheckConstraint, DateTime,
                        create_engine, select,
                        not_, func)

from sqlalchemy.orm import (Session, DeclarativeBase, Mapped,
                            mapped_column, relationship)

import datetime as dt

engine = create_engine('sqlite://alchemy.db', echo=True)


class Base(DeclarativeBase):
    pass

reciept_components = Table(
    'reciept_components',
    Base.metadata, 
    Column('ingredient_id', ForeignKey('ingredients.id'), primary_key=True),
    Column('reciept_id', ForeignKey('reciepts.id'), primary_key=True)
)

reciept_effects = Table(
    'reciept_effects',
    Base.metadata, 
    Column('reciept_id', ForeignKey('reciepts.id'), primary_key=True),
    Column('effect_id', ForeignKey('effects.id'), primary_key=True)
)

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    ingredient_type: Mapped[str]
    rarity: Mapped[str]
    property: Mapped[list[str]]
    reciepts: Mapped[list['Reciept']] = relationship(back_populates='ingredients',
                                                     secondary=reciept_components)

class Reciept(Base):
    __tablename__ = 'reciepts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    potion_type: Mapped[str] = mapped_column(nullable=False)
    complexity: Mapped[str] = mapped_column(CheckConstraint('complexity >= 1 AND complexity <=3'),
                                            nullable=False)
    experiments: Mapped[list['Experiment']] = relationship(back_populates='experiments')
    ingredients: Mapped[list['Ingredient']] = relationship(back_populates='reciepts', 
                                                           secondary=reciept_components)
    effects: Mapped[list['Effect']] = relationship(back_populates='reciepts',
                                                   secondary=reciept_effects)
    
class Effect(Base):
    __tablename__ = 'effects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    reciepts: Mapped[list['Reciept']] = relationship(back_populates='effects',
                                                     secondary=reciept_effects)

class Experiment(Base):
    __tablename__ = 'experiments'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), 
                                              server_default=func.now())
    reciept_id: Mapped[int] = mapped_column(ForeignKey('reciepts.id'))
    reciept: Mapped['Reciept'] = relationship(back_populates='experiments')

Base.metadata.create_all(engine)

if __name__ == '__main__':
    
    with Session(engine) as session:

        # Создаем ингридиенты
        pass