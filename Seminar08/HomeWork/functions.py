def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]

    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.split(",")))
            phone_book.append(record)
    return phone_book


# 1
def print_result(phone_book):
    # print(phone_book)
    for i in range(len(phone_book)):
        if i == 0:
            for j in phone_book[i].keys():
                print(j.ljust(15), end="")
            print("\n")
        for y in phone_book[i].values():
            print(y.ljust(15), end="")
        print("\n")


# 2
def find_by_lastname(phone_book, last_name):
    list1 = []
    for i in phone_book:
        if i.get("Фамилия") == last_name:
            list1.append(i)
    if len(list1) == 0:
        list1 = [
            {
                "Абонента с такой фамилией нет в справочнике!": "Абонента с такой фамилией нет в справочнике!"
            }
        ]
    return list1


# 3
def find_by_number(phone_book, number):
    result = {}
    # list1 = []
    for i in phone_book:
        if i.get("Телефон") == number:
            result = i
            break
        # temp = i.get('Телефон', 'Такого номера нет в справочнике!')
        # if temp == number:
        #     result.update(i)
        #     # list1.append(i)
        else:
            result = {
                "Такого номера нет в справочнике!": "Такого номера нет в справочнике!"
            }
    # return list1
    return list(result.values())


# 4
def add_user(phone_book, user_data):
    fields1 = ["Фамилия", "Имя", "Телефон", "Описание"]
    data = user_data.replace(" ", ",", 3).split(",")
    result = dict(zip(fields1, data))
    print(result)
    phone_book.append(result)


# 5
def change_number(phone_book, last_name, new_number):
    list_of_subscriber = find_by_lastname(phone_book, last_name)
    if len(list_of_subscriber) > 1:
        print(
            f"С данной фамилией найдено {len(list_of_subscriber)} абонентов.\nУкажите порядковый номер абонента для редактирования, в диапазоне от 1 до {len(list_of_subscriber)}."
        )
        print_result(list_of_subscriber)
        n = int(input())
        ind = phone_book.index(list_of_subscriber[n - 1])
    else:
        ind = phone_book.index(list_of_subscriber[0])
    phone_book[ind]["Телефон"] = new_number
    return phone_book[ind]


# 6
def delete_by_number(phone_book, number):
    ind = phone_book.index(find_by_number(phone_book, number))
    return phone_book.pop(ind)


# 7
def write_txt(filename, phone_book):
    # print(phone_book)
    with open(filename, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            temp = phone_book[i].values()
            print(temp)
            s = ""
            for v in phone_book[i].values():
                s += v + ","
            phout.write(
                f"{s[:-1]}" + "\n"
            )  # выдаёт паразитные строки при перезаписи!!!!!!
            # phout.write(f'{s[:-1]}')
