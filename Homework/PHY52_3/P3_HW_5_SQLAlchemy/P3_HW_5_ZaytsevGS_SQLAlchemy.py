from sqlalchemy import (ForeignKey, DateTime, 
                        func, create_engine)

from sqlalchemy.orm import (Session, DeclarativeBase,
                            Mapped, mapped_column,
                            relationship)

import datetime as dt

engine = create_engine('sqlite:///training_diary.db', echo=True)  # Убрать echo после написания


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int]
    workouts: Mapped[list['Workout']] = relationship(back_populates='user')

class Workout(Base):
    __tablename__ = 'workouts'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    date: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), 
                                              server_default=func.now())
    user: Mapped['User'] = relationship(back_populates='workouts')
    workout_details: Mapped[list['WorkoutDetail']] = relationship(back_populates='workout')


class Exercise(Base):
    __tablename__ = 'exercises'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    muscle_group: Mapped[str] = mapped_column(nullable=False)
    workout_details: Mapped[list['WorkoutDetail']] = relationship(back_populates='exercise')

class WorkoutDetail(Base):
    __tablename__ = 'workout_details'

    id: Mapped[int] = mapped_column(primary_key=True)
    workout_id: Mapped[int] = mapped_column(ForeignKey('workouts.id'))
    exercise_id: Mapped[int] = mapped_column(ForeignKey('exercises.id'))
    sets: Mapped[int] = mapped_column(default=0)
    reps: Mapped[str] = mapped_column(default=0)
    workout: Mapped['Workout'] = relationship(back_populates='workout_details')
    exercise: Mapped['Exercise'] = relationship(back_populates='workout_details')


Base.metadata.create_all(engine)

if __name__ == '__main__':

    with Session(engine) as session:

        # Добавляем пользователей в БД
        user_1 = User(name='Дмитрий', age=26)
        user_2 = User(name='Ксения', age=25)

        # Добавляем упражнения в БД
        bench_press = Exercise(name='Жим лежа', muscle_group='грудь')
        deadlift = Exercise(name='Становая тяга', muscle_group='спина')
        squats = Exercise(name='Приседания', muscle_group='ноги')
        pull_ups = Exercise(name='Подтягивания', muscle_group='спина')
        crunches = Exercise(name='Скручивания', muscle_group='пресс')

        # Добавляем тренировки и детали в БД
        user1_w1 = Workout(user=user_1)
        user1_w1_details1 = WorkoutDetail(workout=user1_w1,
                                         exercise=bench_press,
                                         sets=2,
                                         reps='10-8')
        user1_w1_details2 = WorkoutDetail(workout=user1_w1,
                                          exercise=pull_ups,
                                          sets=3,
                                          reps='12-10-8')
        user1_w1_details3 = WorkoutDetail(workout=user1_w1,
                                          exercise=squats,
                                          sets=3,
                                          reps='25-25-20')

        user1_w2 = Workout(user=user_1)
        user1_w2_details1 = WorkoutDetail(workout=user1_w2,
                                         exercise=deadlift,
                                         sets=2,
                                         reps='6-10')
        user1_w2_details2 = WorkoutDetail(workout=user1_w2,
                                          exercise=squats,
                                          sets=4,
                                          reps='25-25-20-15')

        user2_w1 = Workout(user=user_2)
        user2_w1_details1 = WorkoutDetail(workout=user2_w1,
                                         exercise=pull_ups,
                                         sets=3,
                                         reps='15-14-10')
        user2_w1_details2 = WorkoutDetail(workout=user2_w1,
                                          exercise=squats,
                                          sets=3,
                                          reps='30-28-25')
        user2_w1_details3 = WorkoutDetail(workout=user2_w1,
                                          exercise=crunches,
                                          sets=3,
                                          reps='40-35-30')

        user2_w2 = Workout(user=user_2)
        user2_w2_details1 = WorkoutDetail(workout=user2_w2,
                                         exercise=deadlift,
                                         sets=3,
                                         reps='12, 12, 10')
        user2_w2_details2 = WorkoutDetail(workout=user2_w2,
                                          exercise=squats,
                                          sets=4,
                                          reps='25, 25, 20, 20')
        user2_w2_details3 = WorkoutDetail(workout=user2_w2,
                                          exercise=crunches,
                                          sets=4,
                                          reps='40, 35, 30, 25')
        
        #Добавляем все данные в базу
        session.add_all([user_1, user_2, bench_press, deadlift, squats, pull_ups, crunches,
                         user1_w1, user1_w1_details1, user1_w1_details2, user1_w1_details3,
                         user1_w2, user1_w2_details1, user1_w2_details2,
                         user2_w1, user2_w1_details1, user2_w1_details2, user2_w1_details3, 
                         user2_w2, user2_w2_details1, user2_w2_details2, user2_w2_details3
                         ])

        # Сохраняет данные в базу данных
        session.commit()
        print('Данные добавлены в базу данных')
        