import sqlite3 as sl
import logger as lg
import sys

path = 'bd.sqlite'
connection = None


def db_connect():
    global connection

    try:
        connection = sl.connect(path)
    except sl.Error as e:
        print(f'Произошла ошибка: {e}')


db_connect()


def create():
    lg.logging.info('создание таблицы в бд')

    create_users_table = """
    CREATE TABLE IF NOT EXISTS USERS (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER,
      gender TEXT
    );
    """

    with connection:
        connection.execute(create_users_table)

    print(f'{"*" * 50}\n\tТАБЛИЦА В БД СОЗДАНА')


def generation_users():
    lg.logging.info('генерация юзеров')

    sql = 'INSERT INTO USERS (name, age, gender) values(?, ?, ?)'
    data = [
        ('Алиса', 21, 'female'),
        ('Bob', 22, 'male'),
        ('Chris', 23, 'male')
    ]

    with connection:
        connection.executemany(sql, data)

    print(f'{"*" * 50}\n\tДАННЫЕ ДОБАВЛЕНЫ')


def view_users():
    lg.logging.info('просмотр юзеров')
    print(f'{"*" * 50}\n\tПРОСМОТР СОТРУДНИКОВ:')

    with connection:
        data = connection.execute("SELECT * FROM USERS")

    for row in data:
        print(row)


def add_user():
    lg.logging.info('добавление юзера')

    print(f'{"*" * 50}\n\tДОБАВЛЕНИЕ СОТРУДНИКА')
    name = input('Имя: ')
    age = input('Возраст: ')
    gender = input('Пол: ')

    with connection:
        connection.execute(f"INSERT INTO USERS (NAME, AGE, GENDER) VALUES('{name}', '{age}', '{gender}')")

    print('Данные добавлены.')


def edit_user():
    lg.logging.info('редактирование юзера')

    print(f'{"*" * 50}\n\tРЕДАКТИРОВАНИЕ ИНФОРМАЦИИ О СОТРУДНИКЕ')
    user_id = int(input('Введите ID сотрудника для редактирования: '))

    with connection:
        data = connection.execute(f"SELECT * FROM USERS WHERE ID = {user_id}")

    for row in data:
        print(f'Данные сотрудника с ID = {user_id}:\n{row}')
        choice = str(input(
            f'\t\tЧто желаете изменить?\n'
            '\t1. Имя\n'
            '\t2. Возраст\n'
            '\t3. Пол\n'
            '\tВведите номер действия и нажмите Enter: '))
        if choice == '1':
            new_name = str(input('Отредактируйте имя и нажмите Enter: '))
            connection.execute(f"UPDATE USERS SET NAME = '{new_name}' WHERE ID = '{user_id}'")
        elif choice == '2':
            new_age = str(input('Отредактируйте возраст и нажмите Enter: '))
            connection.execute(f"UPDATE USERS SET AGE = '{new_age}' WHERE ID = '{user_id}'")
        elif choice == '3':
            new_gender = str(input('Отредактируйте пол и нажмите Enter: '))
            connection.execute(f"UPDATE USERS SET GENDER = '{new_gender}' WHERE ID = '{user_id}'")
        else:
            print('Что-то пошло не так. Повторите ввод!')

    data = connection.execute(f"SELECT * FROM USERS WHERE ID = {user_id}")
    for row in data:
        print(f'Данные сотрудника с ID = {user_id}:\n{row}')


def delete_user():
    lg.logging.info('удаление юзера')

    print(f'{"*" * 50}\n\tУДАЛЕНИЕ СОТРУДНИКА ИЗ БД')
    user_id = int(input('Введите ID сотрудника для удаления: '))

    with connection:
        connection.execute(f"DELETE FROM USERS WHERE ID = {user_id}")

    print(f'Сотрудник с ID={user_id} удален из базы данных.')


def delete_all():
    lg.logging.info('удаление всех юзеров')
    print(f'{"*" * 50}\n\tОЧИСТКА БД')

    with connection:
        connection.execute("DELETE FROM USERS")


def close_program():
    lg.logging.info('Программа закрыта. Всего ВАМ ДО! БРО! ГО! )))')
    sys.exit('Программа закрыта. Всего ВАМ ДО! БРО! ГО! )))')
    connection.close()
