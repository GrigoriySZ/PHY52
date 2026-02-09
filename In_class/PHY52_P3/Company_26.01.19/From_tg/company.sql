BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Employees" (
	"employee_id"	INTEGER,
	"full_name"	TEXT NOT NULL,
	"hire_date"	DATE,
	"department_id"	INTEGER,
	"contact_id"	INTEGER UNIQUE,
	FOREIGN KEY("department_id") REFERENCES "Departments"("department_id"),
	FOREIGN KEY("contact_id") REFERENCES "Contacts"("contact_id"),
	PRIMARY KEY("employee_id")
);
CREATE TABLE IF NOT EXISTS "Departments" (
	"department_id"	INTEGER,
	"department_name"	TEXT NOT NULL UNIQUE,
	"head_employee_id"	INTEGER UNIQUE,
	"foundation_year"	INTEGER,
	PRIMARY KEY("department_id")
);
CREATE TABLE IF NOT EXISTS "Contacts" (
	"contact_id"	INTEGER,
	"email"	TEXT NOT NULL UNIQUE,
	"phone_number"	TEXT,
	PRIMARY KEY("contact_id")
);
CREATE TABLE IF NOT EXISTS "Projects" (
	"project_id"	INTEGER,
	"project_name"	TEXT NOT NULL UNIQUE,
	"status"	TEXT NOT NULL,
	PRIMARY KEY("project_id")
);
CREATE TABLE IF NOT EXISTS "Tasks" (
	"task_id"	INTEGER,
	"project_id"	INTEGER,
	"task_description"	TEXT NOT NULL,
	"priority"	TEXT,
	"deadline"	DATE,
	FOREIGN KEY("project_id") REFERENCES "Projects"("project_id"),
	PRIMARY KEY("task_id")
);
CREATE TABLE IF NOT EXISTS "ProjectAssignments" (
	"employee_id"	INTEGER,
	"project_id"	INTEGER,
	"assigned_date"	DATE,
	FOREIGN KEY("employee_id") REFERENCES "Employees"("employee_id"),
	FOREIGN KEY("project_id") REFERENCES "Projects"("project_id"),
	PRIMARY KEY("employee_id","project_id")
);
CREATE TABLE IF NOT EXISTS "DepartmentLocations" (
	"department_id"	INTEGER,
	"city"	TEXT NOT NULL,
	"country"	TEXT NOT NULL,
	FOREIGN KEY("department_id") REFERENCES "Departments"("department_id"),
	PRIMARY KEY("department_id")
);
INSERT INTO "Employees" ("employee_id","full_name","hire_date","department_id","contact_id") VALUES (1,'Иванов И.И.','2020-01-15',1,101),
 (2,'Петров П.П.','2021-03-20',1,102),
 (3,'Сидорова С.А.','2019-11-10',2,103),
 (4,'Козлов К.В.','2022-06-01',3,104),
 (5,'Новикова Н.Ю.','2023-01-25',4,105),
 (6,'Левин Л.Л.','2018-08-14',1,106),
 (7,'Федоров Ф.Т.','2020-04-01',5,107),
 (8,'Громова Г.В.','2022-10-10',2,108),
 (9,'Жуков З.И.','2023-05-18',NULL,109),
 (10,'Мишин М.Н.','2021-07-07',4,NULL),
 (11,'Васильев В.Е.','2024-01-01',1,NULL),
 (12,'Егорова Е.М.','2024-02-02',NULL,110);
INSERT INTO "Departments" ("department_id","department_name","head_employee_id","foundation_year") VALUES (1,'Разработка',NULL,2010),
 (2,'Маркетинг',NULL,2012),
 (3,'Финансы',NULL,2008),
 (4,'Продажи',NULL,2015),
 (5,'HR',NULL,2018);
INSERT INTO "Contacts" ("contact_id","email","phone_number") VALUES (101,'ivanov.i@corp.com','555-0101'),
 (102,'petrov.p@corp.com','555-0102'),
 (103,'sidorova.s@corp.com','555-0103'),
 (104,'kozlov.k@corp.com','555-0104'),
 (105,'novikova.n@corp.com','555-0105'),
 (106,'levin.l@corp.com','555-0106'),
 (107,'fedorov.f@corp.com','555-0107'),
 (108,'gromova.g@corp.com','555-0108'),
 (109,'zhukov.z@corp.com','555-0109'),
 (110,'mishin.m@corp.com','555-0110');
INSERT INTO "Projects" ("project_id","project_name","status") VALUES (201,'Мобильное приложение','Active'),
 (202,'Обновление сайта','Active'),
 (203,'Рекламная кампания','Completed'),
 (204,'Бюджетирование Q4','On Hold'),
 (205,'Система аналитики','Active'),
 (206,'Проект-Заглушка','New');
INSERT INTO "Tasks" ("task_id","project_id","task_description","priority","deadline") VALUES (301,201,'Разработка интерфейса','High','2025-05-30'),
 (302,201,'Тестирование бэкенда','High','2025-06-15'),
 (303,202,'Дизайн главной страницы','Medium','2025-04-30'),
 (304,202,'Написание контента','Medium','2025-05-05'),
 (305,203,'Анализ результатов','Low','2024-12-31'),
 (306,205,'Сбор требований','High','2025-04-10'),
 (307,205,'Настройка ETL','Medium','2025-05-20'),
 (308,201,'Fix bug #123','High','2025-04-10'),
 (309,206,'Проверка конфигурации','Low','2025-06-01'),
 (310,NULL,'Административная задача','Low','2025-04-15');
INSERT INTO "ProjectAssignments" ("employee_id","project_id","assigned_date") VALUES (1,201,'2025-03-01'),
 (2,201,'2025-03-01'),
 (2,202,'2025-03-10'),
 (3,203,'2024-11-01'),
 (4,204,'2025-01-01'),
 (5,205,'2025-02-15'),
 (6,201,'2025-03-05'),
 (7,203,'2024-11-01'),
 (8,202,'2025-03-10'),
 (9,205,'2025-02-15');
INSERT INTO "DepartmentLocations" ("department_id","city","country") VALUES (1,'Москва','Россия'),
 (2,'Санкт-Петербург','Россия'),
 (5,'Лондон','Великобритания');
COMMIT;
