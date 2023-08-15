                                                                        #
                                                                        # Вариант 4
                                                                        # Свирякин, Топчей
                                                                        #

import sqlite3 as sq

with sq.connect('dekanat.db') as con:
    cursor = con.cursor()

        # Создание таблицы facultets (факультеты)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facultets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

        # Создание таблицы departments (кафедры)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        id_facultets INT NOT NULL,
        FOREIGN KEY (id_facultets) REFERENCES facultets(id)
    )
    """)
    con.commit()

        # Создание таблицы spec (специальности)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS spec (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        id_departments INT NOT NULL,
        FOREIGN KEY (id_departments) REFERENCES departments(id)
    )
    """)
    con.commit()

        # Создание таблицы subject (предметы)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subject (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

        # Создание таблицы form_s (форма сдачи предмета)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS form_s (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

        # Создание таблицы plan (учебный план)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        spec_id INT NOT NULL,
        subject_id INT NOT NULL,
        form_s_id INT NOT NULL,
        lekc_hours INT NOT NULL,
        pract_hours INT NOT NULL,
        lab_hours INT NOT NULL,
        course_work BOOLEAN NOT NULL,
        FOREIGN KEY (spec_id) REFERENCES spec(id),
        FOREIGN KEY (subject_id) REFERENCES subject(id),
        FOREIGN KEY (form_s_id) REFERENCES form_s(id)
    )
    """)
    con.commit()

        # Создание таблицы applicants (абитуриенты)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applicants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        pol VARCHAR(1) NOT NULL,
        birth_date DATE NOT NULL,
        address VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        email VARCHAR(255) NOT NULL,
        receipt_date DATE NOT NULL,
        speciality VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

with sq.connect('dekanat.db') as con:
    cursor = con.cursor()

        # Заполнение факультетов
    cursor.execute("""INSERT INTO facultets VALUES (1, "Информационные технологии")""")
    cursor.execute("""INSERT INTO facultets VALUES (2, "Экономика")""")
    con.commit()

        # Заполнение кафедр
    cursor.execute("""INSERT INTO departments VALUES (1, "Информационные системы и программирование", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (2, "Обеспечение информационной безопасности телекоммуникационных систем", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (3, "Обеспечение информационной безопасности автоматизированных систем", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (4, "Сетевое и системное администрирование", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (5, "Инфокоммуникационные сети и системы связи", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (6, "Экономика и бухгалтерский учет", 2)""")
    cursor.execute("""INSERT INTO departments VALUES (7, "Банковское дело", 2)""")
    con.commit()

        # Заполнение специальностей
    cursor.execute("""INSERT INTO spec VALUES (1, "Web-разработчик", 1)""")
    cursor.execute("""INSERT INTO spec VALUES (2, "Frontend-разработчик", 1)""")
    cursor.execute("""INSERT INTO spec VALUES (3, "Backend-разработчик", 1)""")
    cursor.execute("""INSERT INTO spec VALUES (4, "Fullstack-разработчик", 2)""")
    cursor.execute("""INSERT INTO spec VALUES (5, "JavaScript-разработчики", 3)""")
    cursor.execute("""INSERT INTO spec VALUES (6, "Системный администратор", 4)""")
    cursor.execute("""INSERT INTO spec VALUES (7, "Python-разработчики", 5)""")
    cursor.execute("""INSERT INTO spec VALUES (8, "Экономист", 6)""")
    cursor.execute("""INSERT INTO spec VALUES (9, "Бухгалтер", 6)""")
    cursor.execute("""INSERT INTO spec VALUES (11, "Менеджер", 8)""")
    con.commit()

        # Заполнение предметов
    cursor.execute("""INSERT INTO subject VALUES (1, "Основы алгоритмизации и программирования")""")
    cursor.execute("""INSERT INTO subject VALUES (2, "Основы проектирования баз данных")""")
    cursor.execute("""INSERT INTO subject VALUES (3, "Основы web-технологий")""")
    cursor.execute("""INSERT INTO subject VALUES (6, "Физическая культура")""")
    cursor.execute("""INSERT INTO subject VALUES (7, "История")""")
    cursor.execute("""INSERT INTO subject VALUES (8, "Стандартизация, сертификация и техническое документирование")""")
    cursor.execute("""INSERT INTO subject VALUES (9, "Дискретная математика с элементами математической логики")""")
    cursor.execute("""INSERT INTO subject VALUES (10, "Теория вероятностей")""")
    con.commit()

        # Заполнение формы сдачи предметов
    cursor.execute("""INSERT INTO form_s VALUES (1, "ЧТО? Что тут надо писать? Я не буду это заполнять")""")
    con.commit()

        # Заполнение формы сдачи предметов
    cursor.execute("""INSERT INTO plan VALUES (1, 0, 1, 0, 1, 0, 1, 0)""")
    con.commit()

        # Заполнение абитуриентов
    cursor.execute("""INSERT INTO applicants VALUES (1, "Свирякин", "Александр", "Сергеевич", "М", "21-09-2005", "г. Ростов-на-Дону", "Номер телефона", "Email", "2023-08-15", "Web-разработчик")""")
    cursor.execute("""INSERT INTO applicants VALUES (2, "Топчей", "Лев", "Саныч", "М", "02-04-2005", "г. Аксай", "66666666666", "Email", "2023-08-15", "Frontend-разработчик")""")
    cursor.execute("""INSERT INTO applicants VALUES (3, "Чичков", "Лил", "Шишивич", "НЕ ОПРЕДЕЛИЛСЯ", "2005-07-22", "г. Шалаш", "Номер телефона", "Email", "2023-08-15", "Fullstack-разработчик")""")
    con.commit()