from datetime import datetime
from handler import Handler
from note import Note

if __name__ == '__main__':
    a = Handler('notes.json')
    a.get()
    print('"Для выхода введите команду - exit"\n"Для добавления заметки введите команду - add"\n"Для редактирования заметки введите команду - update"\n"Для удаления заметки введите команду - delete"\n"Для просмотра заметки введите команду - show"\n"Для просмотра всех заметок введите команду - show all"')
    while True:
        command = input("Введите команду: ")
        if command == "add":
            title = input("Введите название: ")
            msg = input("Введите тело: ")
            a.add(Note(title=title, msg=msg, date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        elif command == "update":
            id = input('Введите индентификатор: ')
            a.update(id)
        elif command == "delete":
            id = input("Введите индентификатор: ")
            a.delete(id)
        elif command == "show":
            id = input("Введите индентификатор: ")
            a.show(id)
        elif command == "show all":
            isFiltered = True if input("Необходим фильтр по дате(Введите + или -): ") == "+" else False
            a.showAll(isFiltered)
        elif command == "exit":
            break
        a.save()