import sqlite3

DB_PATH = 'University.db'

def create_tables(db_path: str):
    """Создается таблицы в базе данных db_path"""

    with sqlite3.connect(db_path) as conn:
        
        conn.execute('''
            CREATE TABLE Faculties (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Financing REAL NOT NULL CHECK (Financing >= 0) DEFAULT 0,
                Name TEXT NOT NULL UNIQUE
            );
        ''')
        
        conn.execute('''
            CREATE TABLE Departments (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Financing REAL NOT NULL CHECK (Financing >= 0) DEFAULT 0,
                Name TEXT NOT NULL UNIQUE,
                FacultyId INTEGER NOT NULL,
                FOREIGN KEY (FacultyId) REFERENCES Faculties(Id)
            );
        ''')

        conn.execute('''
            CREATE TABLE Groups (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL UNIQUE,
                Year INTEGER NOT NULL CHECK (Year BETWEEN 1 AND 5),
                DepartmentId INTEGER NOT NULL,
                FOREIGN KEY (DepartmentId) REFERENCES Departments(Id)
            );
        ''')

        conn.execute('''
            CREATE TABLE Curators (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL CHECK (Name <> ''),
                Surname TEXT NOT NULL CHECK (Surname <> '')
            );
        ''')

        conn.execute('''
            CREATE TABLE GroupsCurators (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                CuratorId INTEGER NOT NULL,
                GroupId INTEGER NOT NULL,
                FOREIGN KEY (CuratorId) REFERENCES Curators(Id),
                FOREIGN KEY (GroupId) REFERENCES Groups(Id)
            );
        ''')

        conn.execute('''
            CREATE TABLE Subjects (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL UNIQUE CHECK (Name <> '')
            );
        ''')

        conn.execute('''
            CREATE TABLE Teachers (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL CHECK (Name <> ''),
                Surname TEXT NOT NULL CHECK (Surname <> ''),
                Salary REAL NOT NULL CHECK (Salary > 0)
            );
        ''')

        conn.execute('''
            CREATE TABLE Lectures (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                LectureRoom TEXT NOT NULL CHECK (LectureRoom <> ''),
                SubjectId INTEGER NOT NULL,
                TeacherId INTEGER NOT NULL,
                FOREIGN KEY (SubjectId) REFERENCES Subjects(Id),
                FOREIGN KEY (TeacherId) REFERENCES Teachers(Id)
            );
        ''')

        conn.execute('''
            CREATE TABLE GroupsLectures (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                GroupId INTEGER NOT NULL,
                LectureId INTEGER NOT NULL,
                FOREIGN KEY (GroupId) REFERENCES Groups(Id),
                FOREIGN KEY (LectureId) REFERENCES Lectures(Id)
            );
        ''')

def fill_tables(db_path):
    """Добавляет данные в таблицы базы данных db_path"""

    with sqlite3.connect(db_path) as conn:

        conn.execute('''
            INSERT INTO Faculties (Financing, Name) VALUES
            (1500000.00, 'Факультет компьютерных наук'),
            (1200000.00, 'Факультет экономики'),
            (900000.00, 'Факультет иностранных языков'),
            (800000.00, 'Факультет математики'),
            (1100000.00, 'Факультет физики'),
            (950000.00, 'Факультет химии'),
            (850000.00, 'Факультет биологии'),
            (700000.00, 'Факультет истории'),
            (750000.00, 'Факультет философии'),
            (1000000.00, 'Факультет психологии');
        ''')

        conn.execute('''
            INSERT INTO Departments (Financing, Name, FacultyId) VALUES
            (300000.00, 'Кафедра программирования', 1),
            (250000.00, 'Кафедра искусственного интеллекта', 1),
            (200000.00, 'Кафедра экономической теории', 2),
            (180000.00, 'Кафедра банковского дела', 2),
            (150000.00, 'Кафедра английского языка', 3),
            (120000.00, 'Кафедра немецкого языка', 3),
            (170000.00, 'Кафедра высшей математики', 4),
            (140000.00, 'Кафедра прикладной математики', 4),
            (160000.00, 'Кафедра теоретической физики', 5),
            (130000.00, 'Кафедра экспериментальной физики', 5);
        ''')

        conn.execute('''
            INSERT INTO Groups (Name, Year, DepartmentId) VALUES
            ('CS-101', 1, 1),
            ('CS-201', 2, 1),
            ('AI-101', 1, 2),
            ('AI-201', 2, 2),
            ('EC-101', 1, 3),
            ('EC-201', 2, 3),
            ('EN-101', 1, 5),
            ('EN-201', 2, 5),
            ('MATH-101', 1, 7),
            ('MATH-201', 2, 7);
        ''')

        conn.execute('''
            INSERT INTO Curators (Name, Surname) VALUES
            ('Иван', 'Петров'),
            ('Мария', 'Сидорова'),
            ('Алексей', 'Иванов'),
            ('Елена', 'Кузнецова'),
            ('Дмитрий', 'Смирнов'),
            ('Ольга', 'Попова'),
            ('Сергей', 'Васильев'),
            ('Наталья', 'Федорова'),
            ('Андрей', 'Морозов'),
            ('Татьяна', 'Волкова');
        ''')

        conn.execute('''
             -- связь многие ко многим 
            INSERT INTO GroupsCurators (CuratorId, GroupId) VALUES
            (1, 1), (1, 2),  -- Один куратор для двух групп
            (2, 3), (2, 4),
            (3, 5), (3, 6),
            (4, 7), (4, 8),
            (5, 9), (5, 10),
            (6, 1),          -- Одна группа с двумя кураторами
            (7, 2),
            (8, 3),
            (9, 4),
            (10, 5);
        ''')

        conn.execute('''
            INSERT INTO Subjects (Name) VALUES
            ('Программирование на C++'),
            ('Базы данных'),
            ('Искусственный интеллект'),
            ('Машинное обучение'),
            ('Экономическая теория'),
            ('Банковское дело'),
            ('Английский язык'),
            ('Немецкий язык'),
            ('Высшая математика'),
            ('Линейная алгебра');
        ''')

        conn.execute('''
            INSERT INTO Teachers (Name, Surname, Salary) VALUES
            ('Александр', 'Ковалев', 2500.00),
            ('Ирина', 'Новикова', 2200.00),
            ('Михаил', 'Павлов', 2800.00),
            ('Светлана', 'Орлова', 2300.00),
            ('Виктор', 'Андреев', 2600.00),
            ('Екатерина', 'Макарова', 2400.00),
            ('Павел', 'Никитин', 2700.00),
            ('Юлия', 'Захарова', 2250.00),
            ('Артем', 'Белов', 2900.00),
            ('Анна', 'Тихонова', 2350.00);
        ''')

        conn.execute('''
            INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId) VALUES
            ('Аудитория 101', 1, 1),
            ('Аудитория 102', 2, 2),
            ('Аудитория 103', 3, 3),
            ('Аудитория 104', 4, 4),
            ('Аудитория 201', 5, 5),
            ('Аудитория 202', 6, 6),
            ('Аудитория 203', 7, 7),
            ('Аудитория 204', 8, 8),
            ('Аудитория 301', 9, 9),
            ('Аудитория 302', 10, 10),
            ('Аудитория 303', 1, 1),  -- Дополнительные лекции
            ('Аудитория 304', 2, 2),
            ('Аудитория 401', 3, 3),
            ('Аудитория 402', 4, 4),
            ('Аудитория 403', 5, 5);
        ''')

        conn.execute('''
            --  связь многие ко многим 
            INSERT INTO GroupsLectures (GroupId, LectureId) VALUES
            (1, 1), (1, 2),   -- Группа посещает несколько лекций
            (2, 3), (2, 4),
            (3, 5), (3, 6),
            (4, 7), (4, 8),
            (5, 9), (5, 10),
            (6, 11), (6, 12), -- Лекция посещается несколькими группами
            (7, 13), (8, 13),
            (9, 14), (10, 14),
            (1, 15), (2, 15),
            (3, 1), (4, 2);   -- Перекрестные связи
        ''')

        conn.commit()

def show_groups_and_departments(db_path):
    """Выводит список всех групп. 
    
    Задача: Выводит список всех групп (их названия)
    вместе с названиями кафедр, к которым они относятся.
    Отсортировать результат по названию кафедры,
    а затем по названию группы.

    """
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT g.Name, d.Name FROM Groups g
            JOIN Departments d
            ON g.DepartmentId = d.Id
            ORDER BY d.Name, g.Name;
        ''')

        group_list = cursor.fetchall()

        print('Список всех групп в университете')
        for index, (g_name, d_name) in enumerate(group_list, 1):
            print(f'- {index:2}. Группа: {g_name}\tФакультет: {d_name}')


def show_lectures_and_rooms(db_path):
    """Выводит список всех лекций. 
    
    Задача: Выводит список всех лекций (аудитория и ID)
    вместе с названиями предмета и
    фамилии преподавателя, который их ведет.
    Отсортировать по названию предмета.

    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT l.LectureRoom, s.Name, t.Name
            FROM Lectures l
            JOIN Subjects s
            ON l.SubjectId = s.Id
            JOIN Teachers t
            ON l.TeacherId = t.Id
            ORDER BY s.Name;
        ''')

        lecture_list = cursor.fetchall()

        print('Список всех лекций:')
        for index, (room, subject, teacher) in enumerate(lecture_list, 1):
            print(f'- {index:2}. {room}: "{subject}"\n L  Преподаватель: {teacher}')

def show_curators_without_group(db_path):
    """Выводит список всех кураторов без группы.

    Задача: Найти всех кураторов, которые не прикреплены ни к одной группе.
    Вывести их имя и фамилию

    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT c.Name, c.Surname FROM Curators c
            JOIN GroupsCurators gc
            ON c.Id = gc.CuratorId
            WHERE NOT c.Id = gc.CuratorId;
        ''')

        curators_list = cursor.fetchall()

        print('Список кураторов, которые не прикреплены к группам:')
        if curators_list:
            for index, (curator_name, surname) in enumerate(curators_list, 1):
                print(f'- {index:2}. {curator_name} {surname}')
        else:
            print('- Все кураторы прикреплены к группам.')

def show_full_groups_info(db_path):
    """Выводит полную информацию о группах.

    Задача: Вывести полную информацию о группах:
    Название группы, год обучения, название кафедры и
    название факультета, к которому относится кафедра.

    """
    with (sqlite3.connect(db_path) as conn):
        cursor = conn.cursor()

        cursor.execute('''
            SELECT g.Name, g.Year, d.Name, f.Name 
            FROM Groups g
            JOIN Departments d
            ON g.DepartmentId = d.Id
            JOIN Faculties f
            ON d.FacultyId = f.Id;
        ''')

        groups_list = cursor.fetchall()

        print('Информация о группах:')
        for index, (group_name, year, depart_name, faculty_name) in enumerate(groups_list, 1):
            print(f'{index:2}. - Группа: {group_name}, Год: {year}')
            print(f'    L Кафедра: {depart_name}')
            print(f'    L Факультет: {faculty_name}')

def show_group_with_high_financing(db_path):
    """Выводит название групп с финансированием больше 170 000.

    Задача: Вывести название всех групп, которые относятся к кафедрам
    с финансированием более 170 000. Показать название группы
    и финансирование её кафедры.

    """
    with (sqlite3.connect(db_path) as conn):
        cursor = conn.cursor()

        cursor.execute('''
            SELECT g.Name, d.Financing FROM Groups g
            JOIN Departments d
            ON g.DepartmentId = d.Id
            WHERE d.Financing > 170_000;
        ''')

    groups_and_financing_list = cursor.fetchall()

    print('Список групп с финансированием:')
    for index, (group_name, financing) in enumerate(groups_and_financing_list, 1):
        print(f'{index:2}. - Группа: {group_name}')
        print(f'    L Финансирование кафедры: {financing:.2f}')

if __name__ == '__main__':

    # create_tables(DB_PATH)
    # fill_tables(DB_PATH)
    # show_groups_and_departments(DB_PATH)
    # show_lectures_and_rooms(DB_PATH)
    # show_curators_without_group(DB_PATH)
    # show_full_groups_info(DB_PATH)
    show_group_with_high_financing(DB_PATH)