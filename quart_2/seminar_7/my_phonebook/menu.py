import csv_action as ca


def menu():
    print('*' * 35)
    print('\t\tСПИСОК ДЕЙСТВИЙ:')
    print('\t1. Показать все контакты')
    print('\t2. Сгенерировать контакты')
    print('\t3. Добавить контакт')
    print('\t4. Удалить все контакты')
    print('\t5. Закрыть программу')
    print('*' * 35)
    choice = int(input('\tВведите номер действия: '))

    if choice == 1:
        ca.view_csv()
    elif choice == 2:
        ca.generate_fake_contact()
    elif choice == 3:
        ca.add_new_contact()
    elif choice == 4:
        ca.delete_all()
    elif choice == 5:
        exit()
    else:
        print('Что-то пошло не так. Повторите ввод!')

