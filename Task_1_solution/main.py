# Домашнее задание. 
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def add_person():
    name_first = input('Введите имя: ')
    name_last = input('Введите фамилию: ')
    phone_num = input('Введите телефон: ')
    with open('phone_book.txt', 'a', encoding='utf-8') as book:
        book.write(f'{name_first} {name_last} {phone_num}\n')

def create_file():
    with open('phone_book.txt', 'w', encoding='utf-8') as book:
        book.write('Имя  Фамилия Телефон\n')

def search_name():
    name_search = input('Введите имя для поиска: ')
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            if name_search.lower() == line.strip('\n').split()[0].lower():
                return line
        return "Запись не найдена"
    
def search_surname():
    surname_search = input('Введите фамилию для поиска: ')
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            if surname_search.lower() == line.strip('\n').split()[1].lower():
                return line
        return "Запись не найдена"            

def search_phone():
    phone_search = input('Введите телефон для поиска: ')
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            if phone_search.lower() == line.strip('\n').split()[2].lower():
                return line
        return "Запись не найдена"
    
def delete_person():
    person_delete = input('Введите имя или фамилию для удаления данных: ')
    answer = 'Запись не найдена'
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        lines = book.readlines()
    with open('phone_book.txt', 'w', encoding='utf-8') as book:
        for line in lines:
            if person_delete.lower() != line.strip('\n').split()[0].lower() and person_delete.lower() != line.strip('\n').split()[1].lower(): 
                book.write(line)
            else: 
                answer = 'Запись удалена' 
    return answer
    
def edit_person():
    person_edit = input('Введите имя или фамилию для изменения данных: ')
    answer = 'Запись не найдена'
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        lines = book.readlines()
    with open('phone_book.txt', 'w', encoding='utf-8') as book:
        for line in lines:
            if person_edit.lower() != line.strip('\n').split()[0].lower() and person_edit.lower() != line.strip('\n').split()[1].lower(): 
                book.write(line)
            else:
                name_first = input('Введите имя: ')
                name_last = input('Введите фамилию: ')
                phone_num = input('Введите телефон: ')
                book.write(f'{name_first} {name_last} {phone_num}\n') 
                answer = 'Запись изменена' 
    return answer

def main():
    print('1) Создать файл телефонной книги ',
          '2) Добавить запись в телефонную книгу',
          '3) Найти запись по имени',
          '4) Найти запись по фамилии',
          '5) Найти запись по телефону',
          '6) Удалить запись в телефонной книге',
          '7) Изменить запись в телефонной книге',
          '8) Выход', sep='\n', end='\n')
    match input():
        case '1':
            create_file()
        case '2':
            add_person()
        case '3':
            print(search_name())
        case '4':
            print(search_surname())
        case '5':
            print(search_phone())
        case '7':
            print(edit_person())     #изменить данные в файле
        case '6':
            print(delete_person())   #удалить данные из файла
        case _:
            print("Good bye")

main()

