from sqlalchemy import (ForeignKey, Table, Column,
                        String, Float, Integer,
                        CheckConstraint, DateTime,
                        create_engine, select,
                        not_, and_, func, Sequence)
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import (Session, DeclarativeBase, Mapped,
                            mapped_column, relationship)
from datetime import datetime, timedelta

from sqlalchemy.util import ro_memoized_property

DB_PATH = 'alchemy.db'

engine = create_engine(f'sqlite:///{DB_PATH}')


class Base(DeclarativeBase):
    pass

recipe_ingredients = Table(
    'recipe_ingredients',
    Base.metadata, 
    Column('ingredient_id', ForeignKey('ingredients.id'), primary_key=True),
    Column('recipe_id', ForeignKey('recipes.id'), primary_key=True)
)

recipe_effects = Table(
    'recipe_effects',
    Base.metadata, 
    Column('recipe_id', ForeignKey('recipes.id'), primary_key=True),
    Column('effect_id', ForeignKey('effects.id'), primary_key=True)
)

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str]
    cost: Mapped[int] = mapped_column(CheckConstraint('cost >= 0'))
    location: Mapped[str]
    recipes: Mapped[list['Recipe']] = relationship(back_populates='ingredients',
                                                     secondary=recipe_ingredients)

class Recipe(Base):
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str] = mapped_column(nullable=False)
    experiments: Mapped[list['Experiment']] = relationship(back_populates='recipe')
    ingredients: Mapped[list['Ingredient']] = relationship(back_populates='recipes', 
                                                           secondary=recipe_ingredients)
    effects: Mapped[list['Effect']] = relationship(back_populates='recipes',
                                                   secondary=recipe_effects)
    
class Effect(Base):
    __tablename__ = 'effects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    recipes: Mapped[list['Recipe']] = relationship(back_populates='effects',
                                                     secondary=recipe_effects)

class Experiment(Base):
    __tablename__ = 'experiments'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                              server_default=func.now())
    success: Mapped[bool] = mapped_column(default=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey('recipes.id'))
    recipe: Mapped['Recipe'] = relationship(back_populates='experiments')

Base.metadata.create_all(engine)

def get_recipe_with_ingredient(session: Session, recipe_effect: str,ingredient: str):
    """
    Выводит все рецепты зелий лечения, для которых нужен корень мандрагоры

    Arguments:
        session(Session): Сессия для запроса к базе данных
        recipe_effect(str): Эффект зелья
        ingredient(str): Ингредиент, используемый для создания зелья

    """
    if not isinstance(recipe_effect, str) or not recipe_effect.strip():
        print(f'Error: Некорректный аргумент recipe_effect: arg: "{recipe_effect}", type: "{type(recipe_effect)}"!')
        return None

    if not isinstance(ingredient, str) or not ingredient.strip():
        print(f'Error: Некорректный аргумент ingredient: arg: "{ingredient}", type: "{type(ingredient)}"!')
        return None

    _recipe_effect = recipe_effect.strip().lower()
    _ingredient = ingredient.strip().lower()

    try:
        query = (
            select(Recipe.name, Effect.name)
            .join(Recipe.effects)
            .join(Recipe.ingredients)
            .where(Effect.name == _recipe_effect,
                        Ingredient.name == _ingredient)
            .order_by(Recipe.name)
        )

        # Возвращаем данные из таблицы
        return session.scalars(query).all()
    except NoResultFound:
        print(f'Рецептов с {ingredient} не найдено')
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None

def get_failed_exp(session: Session, days_ago: int):
    """
    Выдает все неудачные эксперименты за последний месяц и использованные рецепты

    Arguments:
        session(Session): Сессия для запроса к базе данных
        days_ago(int): Интервал для просмотра всех неудачных экспериментов в днях
    
    """
    if not isinstance(days_ago, int):
        print(f'Error: Аргумент days_ago должен быть задан в виде числа. arg: "{days_ago}", type: "{type(days_ago)}"!')
        return None
    elif days_ago < 0:
        print(f'Интервал просмотра days_ago не может быть отрицательным. arg: "{days_ago}"')
        return None

    thirty_days_ago = datetime.today() - timedelta(days=days_ago)

    query = (
        select(Experiment.id, Experiment.date, Recipe.name)
        .join(Experiment.recipe)
        .where(Experiment.success == False,
                    Experiment.date >= thirty_days_ago)
        .order_by(Experiment.date.desc())
    )

    return session.execute(query).all()

def get_most_expensive_recipe(session: Session):
    """
    Выводит самый дорогой рецепт по стоимости ингредиентов

    """
    try:
        subquery = (
            select(Recipe.id.label('recipe_id'),
                   func.sum(Ingredient.cost).label('total_cost')
                   )
            .join(Recipe.ingredients)
            .group_by(Recipe.id)
            .subquery()
        )

        max_cost_subquery = (
            select(func.max(subquery.c.total_cost))
            .scalar_subquery()
        )

        query = (
            select(Recipe.name, subquery.c.total_cost)
            .join(subquery, Recipe.id == subquery.c.recipe_id)
            .where(subquery.c.total_cost == max_cost_subquery)
        )

        return session.execute(query).all()
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':

    print('Создаю базу данных...')
    # Создаем и заполняем БД
    with Session(engine) as session:

        # Создаем ингредиенты
        mandrake_root = Ingredient(name='корень мандрагоры', type='растение', cost=10, location='леса')
        wheat = Ingredient(name='пшеница', type='растение', cost=5, location='поля')
        daedra_heart = Ingredient(name='сердце даэдра', type='монстр', cost=250, location='Обливион')
        blue_mountain_flower = Ingredient(name='голубой горноцвет', type='растение', cost=2, location='горы')
        blisterwort = Ingredient(name='лютый гриб', type='гриб', cost=12, location='леса')
        falmer_ear = Ingredient(name='ухо фалмера', type='монстр', cost=10, location='пещеры')
        moon_sugar = Ingredient(name='лунный сахар', type='субстанция', cost=50, location='пустыни')
        frost_salts = Ingredient(name='морозная соль', type='субстанция', cost=100, location='горы')
        juniper_berries = Ingredient(name='ягоды можжевельника', type='растение', cost=1, location='горы')
        vampire_dust = Ingredient(name='прах вампира', type='монстр', cost=25, location='болота')
        luna_moth_wing = Ingredient(name='крыло лунного мотылька', type='насекомое', cost=5, location='поля')

        # Создаем рецепты
        magic_health_potion = Recipe(name='волшебное зелье восстановления здоровья', type='зелье')
        strong_health_porion = Recipe(name='могучее зелье восстановления здоровья', type='зелье')
        berserker_potion = Recipe(name='зелье берсерка', type='яд')
        nordic_potion = Recipe(name='нордическое зелье', type='яд')
        night_cure_potion = Recipe(name='зелье ночного исцеления', type='зелье')

        # Создаем эффекты
        restore_health = Effect(name='восстановление здоровья')
        resist_magic = Effect(name='сопротивление магии')
        resist_frost = Effect(name='сопротивление холоду')
        fortify_health = Effect(name='повышение здоровья')
        damage_health = Effect(name='урон здоровью')
        frenzy = Effect(name='бешенство')
        weakness_of_fire = Effect(name='уязвимость к огню')
        cure_disease = Effect(name='исцеление болезней')
        invisibility = Effect(name='невидимость')
        fear = Effect(name='страх')

        # Создаем эксперименты
        time_format = '%Y-%m-%d %H:%M'
        exp_date = lambda date: datetime.strptime(date, time_format)

        magic_health_potion_exp_1 = Experiment(date=exp_date('2025-12-28 12:10'),
                                               success=False, recipe=magic_health_potion)
        berserker_potion_exp_1 = Experiment(date=exp_date('2026-01-15 21:15'),
                                            success=True, recipe=berserker_potion)
        magic_health_potion_exp_2 = Experiment(date=exp_date('2026-01-16 18:50'),
                                               success=True, recipe=magic_health_potion)
        night_cure_potion_exp_1 = Experiment(date=exp_date('2026-01-29 10:30'),
                                             success=False, recipe=night_cure_potion)
        night_cure_potion_exp_2 = Experiment(date=exp_date('2026-01-30 01:10'),
                                             success=True, recipe=night_cure_potion)
        nordic_potion_exp_1 = Experiment(date=exp_date('2026-02-10 22:50'),
                                         success=True, recipe=nordic_potion)
        strong_health_porion_exp_1 = Experiment(date=exp_date('2026-02-10 22:50'),
                                                success=False, recipe=strong_health_porion)

        # добавляем эффекты рецептам в ассоциативную таблицу
        magic_health_potion.effects.append(restore_health)
        magic_health_potion.effects.append(resist_magic)

        strong_health_porion.effects.append(restore_health)
        strong_health_porion.effects.append(fortify_health)

        berserker_potion.effects.append(fortify_health)
        berserker_potion.effects.append(frenzy)
        berserker_potion.effects.append(damage_health)

        nordic_potion.effects.append(resist_frost)
        nordic_potion.effects.append(weakness_of_fire)

        night_cure_potion.effects.append(cure_disease)
        night_cure_potion.effects.append(invisibility)
        night_cure_potion.effects.append(fear)

        # добавляем ингредиенты рецептам в ассоциативную таблицу
        magic_health_potion.ingredients.append(mandrake_root)
        magic_health_potion.ingredients.append(wheat)
        magic_health_potion.ingredients.append(blue_mountain_flower)

        strong_health_porion.ingredients.append(mandrake_root)
        strong_health_porion.ingredients.append(wheat)
        strong_health_porion.ingredients.append(daedra_heart)

        berserker_potion.ingredients.append(mandrake_root)
        berserker_potion.ingredients.append(blisterwort)
        berserker_potion.ingredients.append(falmer_ear)

        nordic_potion.ingredients.append(moon_sugar)
        nordic_potion.ingredients.append(frost_salts)
        nordic_potion.ingredients.append(juniper_berries)

        night_cure_potion.ingredients.append(vampire_dust)
        night_cure_potion.ingredients.append(luna_moth_wing)
        night_cure_potion.ingredients.append(daedra_heart)

        print(f'Добавлю записи в "{DB_PATH}...')
        print(f'Добавляем ингредиент...')
        session.add_all([mandrake_root, wheat, daedra_heart, blue_mountain_flower,
                         blisterwort, falmer_ear, moon_sugar, frost_salts,
                         juniper_berries, vampire_dust, luna_moth_wing])

        print(f'Добавляем эффекты...')
        session.add_all([restore_health, resist_magic, resist_frost, fortify_health,
                         damage_health, frenzy, weakness_of_fire, cure_disease,
                         invisibility, fear])

        print(f'Добавляем эксперименты...')
        session.add_all([magic_health_potion_exp_1, berserker_potion_exp_1,
                         magic_health_potion_exp_2, night_cure_potion_exp_1,
                         night_cure_potion_exp_2, nordic_potion_exp_1,
                         strong_health_porion_exp_1])

        print(f'Добавляем рецепты...')
        session.add_all([magic_health_potion, strong_health_porion, berserker_potion,
                         nordic_potion, night_cure_potion])

        # Сохраняем в БД
        session.commit()
        print(f'Данные добавлены в "{DB_PATH}".')

    with Session(engine) as session:
        recipe_effect = 'Восстановление здоровья'
        ingredient = 'Корень мандрагоры'

        recipes = get_recipe_with_ingredient(session,
                                             recipe_effect=recipe_effect,
                                             ingredient=ingredient)
        if recipes:
            print(f'\nСписок зелий с эффектом "{recipe_effect}" и ингредиентом "{ingredient}":')
            for i, recipe in enumerate(recipes, 1):
                print(f'{i:2}. Рецепт: {recipe.capitalize()}')
        else:
            print(f'В базе нет зелий с эффектом "{recipe_effect}" и ингредиентом "{ingredient}".')

    with Session(engine) as session:

        days_ago = 30
        formatter = '%H:%M %d.%m.%Y г.'

        failed_exp = get_failed_exp(session, days_ago)
        if failed_exp:
            print(f'\nСписок неудачных экспериментов с рецептами за последние {days_ago} дней:')
            for i, (exp_id, exp_date, recipe_name) in enumerate(failed_exp, 1):
                print(f'{i:2}. Эксперимент #{exp_id} - Рецепт: "{recipe_name.capitalize()}". Время: {exp_date.strftime(formatter)}')
        else:
            print('В базе нет неудачных экспериментов.')

    with Session(engine) as session:

        most_expensive = get_most_expensive_recipe(session)
        if most_expensive:
            print('\nСписок самых дорогих рецептов по цене ингредиентов:')
            for i, (recipe_name, total_cost) in enumerate(most_expensive, 1):
                print(f'{i:2}. Рецепт: {recipe_name}. Общая стоимость ингредиентов: {total_cost:.2f}')
        else:
            print('В базе данных нет рецептов!')