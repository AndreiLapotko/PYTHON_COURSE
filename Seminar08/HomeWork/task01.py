
def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phonebook.csv')

    while choice != 8:

        if choice == 1:
            print_result(phone_book)

        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))

        elif choice == 3:
            number = input('number ')
            print(find_by_number(phone_book, number))

        elif choice == 4:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.csv', phone_book)

        elif choice == 5:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))

        elif choice == 6:
            last_name = input('lastname ')
            print(delete_by_lastname(phone_book, last_name))

        elif choice == 7:
            write_txt('phonebook.csv', phone_book)

        choice = show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник.\n"
          "2. Найти абонента по фамилии.\n"
          "3. Найти абонента по номеру телефона.\n"
          "4. Добавить абонента в справочник.\n"
          "5. Редактировать существующего абонента.\n"
          "6. Удаление абонента по фамилии.\n"
          "7, Сохранить справочник в текстовом формате.\n"
          "8. Закончить работу.\n")
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book



def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')


def print_result(phb):
    for i in range(len(phb)):
            s = ''
            for v in phb[i].values():
                s += v + ",\t"
            print(f'{s[:-2]}')

work_with_phonebook()