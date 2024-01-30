from datetime import datetime
from handler import Handler
from note import Note

if __name__ == '__main__':
    a = Handler('notes.json')
    a.get()
    print('"Для выхода введите команду - exit"\n"Для добавления заметки введите команду - add"')
    while True:
        command = input("Введите команду: ")
        if command == "add":
            title = input("Введите название: ")
            msg = input("Введите тело: ")
            a.add(Note(title=title, msg=msg, date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        elif command == "exit":
            break
        a.save()
    
    
