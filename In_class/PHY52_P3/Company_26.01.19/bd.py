from datetime import date

# Примерный стинтаксис
#  
#  SELECT columb, agregate_func as name FROM table - Выибираем источник выборки
# WHERE condition - определяем область выборки в источнике
# GROUP BY column - группировка по какому-то принципу
# HAVING condition - фильрует после группировки отфильтровать по определенному принципу

# Агрегатные функции можно использовать для фильтрации после HAVING

'''
SELECT Employee, SUM(Amount) as TotalAmount 
FROM sales
GROUP BY Employee
HAVING TotalAmount > 300;
'''

'''
SELECT Employee, SUM(Amount) as TotalAmount 
FROM sales
GROUP BY Employee
HAVING TotalAmount > AVG(Amount);
'''

import sqlite3

db_path = 'company.db'

def run_having(db_path):

    with sqlite3.connect(db_path) as conn:
        coursor = conn.cursor()
        coursor.execute('''
            SELECT department_id FROM employees
            GROUP BY department_id
            HAVING COUNT(employee_id) > 2;
        ''')

        print(f'Task1: {coursor.fetchall()}')

        coursor.execute('''
            SELECT project_id FROM tasks
            GROUP BY project_id
            HAVING MAX(deadline) > '2025-06-01';
        ''')

        print(f'Task3: {coursor.fetchall()}')

        coursor.execute('''
            SELECT distinct project_id FROM ProjectAssignments
            WHERE assigned_date < '2025-02-01'
        ''')
        # distinct - выводит только уникальные результаты запроса 
        # пишется только после SELECT

        print(f'Task4: {coursor.fetchall()}')

        coursor.execute('''
            SELECT employee_id FROM ProjectAssignments
            GROUP BY employee_id
            HAVING COUNT(project_id) = 2;
        ''')

        print(f'Task5: {coursor.fetchall()}')


# INNER JOIN или JOIN/LEFT JOIN - объединения

# Синтаксис: 
# 
# SELECT column1, column2 
# FROM table1 
# JOIN table2 
# ON table1.id = table2.id 

# Пример INNER JOIN/JOIN: 
# SELECT group_name FROM faculties 
# JOIN students 
# ON faculties.group_id = students.group_id 
# WHERE name = 'Мария';

# INNER JOIN возвращает записи, у которых есть совпадения в обеих таблицах
# LEFT JOIN - все записи из левой таблицы и подходящие из правой

def run_join(db_path):

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT e.full_name, d.department_name 
            FROM Employees e
            INNER JOIN Departments d
            ON e.department_id = d.department_id;
        ''')

        # print(f'Task1: {coursor.fetchall()}')

        cursor.execute('''
            SELECT full_name, email 
            FROM employees e 
            LEFT JOIN contacts c
            ON e.contact_id = c.contact_id
        ''')

        # print(f'Task2: {coursor.fetchall()}')

        cursor.execute('''
            SELECT p.project_name, COUNT(pa.employee_id) 
            AS count_emp_project
            FROM projects p
            LEFT JOIN projectassignments pa
            ON p.project_id = pa.project_id
            GROUP BY p.project_id
        ''')

        # print(f'Task3: {coursor.fetchall()}')

        cursor.execute('''
            SELECT e.full_name, d.department_name, dl.city
            FROM employees e
            JOIN departments d
            ON e.department_id = d.department_id
            JOIN departmentlocations dl
            ON d.department_id = dl.department_id;
        ''')

        # print(f'Task4: {coursor.fetchall()}')

        cursor.execute('''
            SELECT d.department_name, COUNT(e.employee_id) as count_staff
            FROM departments d
            JOIN employees e
            ON d.department_id = e.department_id
            GROUP BY d.department_id
            HAVING count_staff > 2;
        ''')

        print(f'Task5: {cursor.fetchall()}')


# SELECT col FROM table 
# WHERE col OPERATOR (
#   SELECT col FROM table
#   WHERE condition
# )
# () - подзапрос делается в руглых скобках
# SELETC сначала начинает операцию с самого глубокого подзапроса во вложенности
# 
# SELECT вовзращает один из типов: 
# 1) Скаляр - одно значение
# 2) Список
# 3) Таблица

def run_queris(db_path):

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT e.full_name FROM Employees e
            JOIN ProjectAssignments pa
            ON e.employee_id = pa.employee_id
            JOIN Projects p
            ON pa.project_id = p.project_id
            WHERE p.status = 'Active'
            GROUP BY e.employee_id
            HAVING COUNT(p.project_id) > 1;
        ''')

        print(f'Task 1: {cursor.fetchall()}')

        cursor.execute('''
            SELECT e.full_name FROM Employees e
            WHERE e.employee_id IN (
                SELECT pa.employee_id FROM ProjectAssignments pa
                WHERE pa.project_id IN (
                    SELECT p.project_id FROM Projects p
                    WHERE p.status = 'Active'
                )
                GROUP BY pa.employee_id
                HAVING COUNT(pa.project_id) > 1
            );
        ''')

        print(f'Task 1 with queris: {cursor.fetchall()}')

        current_year = date.today().year

        cursor.execute(f'''
            SELECT d.department_name FROM Departments d
            JOIN Employees e
            ON d.department_id = e.department_id
            GROUP BY d.department_id
            HAVING AVG({current_year}-strftime('%Y', e.hire_date)) > (
                SELECT AVG({current_year}-strftime('%Y', e.hire_date)) 
                FROM Employees e
                )
        ''')

        print(f'Task 2: {cursor.fetchall()}')
    
        cursor.execute('''
            SELECT p.project_name FROM Projects p
            WHERE p.project_id NOT IN (
                SELECT p.project_id FROM Projects p
                JOIN ProjectAssignments pa
                ON p.project_id = pa.project_id
                JOIN Employees e
                ON pa.employee_id = e.employee_id
                JOIN Departments d
                ON e.department_id = d.department_id
                WHERE d.department_name = 'Разработка'
                )
        ''')

        print(f'Task 3: {cursor.fetchall()}')

        cursor.execute('''
            SELECT dl.country FROM DepartmentLocations dl
            JOIN Employees e
            ON dl.department_id = e.department_id
            JOIN ProjectAssignments pa
            ON e.employee_id = pa.employee_id
            JOIN Tasks t
            ON pa.project_id = t.project_id
            WHERE t.priority = 'High'
            GROUP BY dl.country
            HAVING COUNT(t.task_id) > 2; 
        ''')

        print(f'Task 4: {cursor.fetchall()}')

        cursor.execute('''
            SELECT d.department_name FROM Departments d
            WHERE EXISTS (
                SELECT 1 FROM DepartmentLocations dl
                WHERE dl.department_id = d.department_id
                )
        ''')

        print(f'Task E3: {cursor.fetchall()}')

        cursor.execute('''
            SELECT AVG(task_count) FROM 
                (SELECT COUNT(task_id) as task_count 
                FROM Tasks
                GROUP BY project_id) as tmp_table
        ''')

        print(f'Task E4_A: {cursor.fetchall()}')

        """1.А. Найти всех сотрудников, работающих в департаменте
        «Разработка» Вместо того чтобы вручную искать ID департамента, мы
        получаем его подзапросом."""

        cursor.execute('''
            SELECT e.full_name FROM Employees e
            WHERE e.department_id IN (
                SELECT d.department_id FROM Departments d
                WHERE d.department_name = 'Разработка')
        ''')
        
        print(f'Task E1_A: {cursor.fetchall()}')

        """1.Б. Найти проекты, в которых есть задачи с «Высоким» (High)
        приоритетом Здесь используется оператор IN, так как подзапрос
        может вернуть несколько ID проектов."""

        cursor.execute('''
            SELECT p.project_name FROM Projects p
            WHERE p.project_id IN (
                SELECT t.project_id FROM Tasks t
                WHERE t.priority = 'High'
                )
        ''')

        print(f'Task E1_Б: {cursor.fetchall()}')

        """2.А. Вывести список сотрудников и количество проектов, на
        которые они назначены"""
        
        cursor.execute('''
            SELECT e.full_name, (
            SELECT COUNT(*) FROM ProjectAssignments pa
            WHERE pa.employee_id = e.employee_id
            ) as count_project
           FROM Employees e
        ''')

        print(f'Task E2_A: {cursor.fetchall()}')


if __name__ == '__main__':

    # run_having(db_path)
    # run_join(db_path)
    run_queris(db_path)