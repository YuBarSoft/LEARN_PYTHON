import connect_sqlite as conn


def run():
    while True:
        choice = str(input(
            f'{"*" * 50}\n'
            '\t\tСПИСОК ДЕЙСТВИЙ:\n'
            '\t1. Создать пустую БД\n'
            '\t2. Сгенерировать сотрудников\n'
            '\t3. Показать всех сотрудников\n'
            '\t4. Добавить сотрудника\n'
            '\t5. Отредактировать сотрудника\n'
            '\t6. Удалить сотрудника\n'
            '\t7. Очистить БД\n'
            '\t8. Закрыть программу\n'
            f'{"*" * 50}\n'
            '\tВведите номер действия и нажмите Enter: '))

        if choice == '1':
            conn.create()
        elif choice == '2':
            conn.generation_users()
        elif choice == '3':
            conn.view_users()
        elif choice == '4':
            conn.add_user()
        elif choice == '5':
            conn.edit_user()
        elif choice == '6':
            conn.delete_user()
        elif choice == '7':
            conn.delete_all()
        elif choice == '8':
            conn.close_program()
        else:
            print('Что-то пошло не так. Повторите ввод!')

