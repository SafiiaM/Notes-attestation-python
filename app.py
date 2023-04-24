import datetime
from colorama import Fore, Style

from controller import Controller
from modelJSON import ModelJSON
from note import Note
from view import View


def run():
    c = Controller(ModelJSON("notes.json"), View())

    while True:
        command = input(Fore.BLUE +
                        '1 - Create a note\n'
                        '2 - Read a note\n'
                        '3 - Update a note\n'
                        '4 - Delete a note\n'
                        '5 - Delete all the notes\n'
                        '6 - Read all the notes\n'
                        '7 - Exit\n' +
                        'Make your choice please: '
                        + Style.RESET_ALL)
        if command == '7':
            break

        if command == '1':
            print(Fore.GREEN + 'Create a note:' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            print(Fore.GREEN + 'Read a note:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif command == '3':
            if c.notes_exist():
                print(Fore.YELLOW + 'Update a note:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + 'Delete a note:' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif command == '5':
            if c.notes_exist():
                print(Fore.RED + 'Delete all the notes:' + Style.RESET_ALL)
                if input(Fore.RED + 'Are you sure you want to delete all the notes? (Y/N): '
                         + Style.RESET_ALL).capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif command == '6':
            if c.notes_exist():
                print(Fore.BLUE + 'List of all the notes:' + Style.RESET_ALL)
                c.show_notes()
        else:
            print(Fore.RED + 'The command is not found' + Style.RESET_ALL)


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Enter the name of the note: ')
    text = input('Enter the body of the note: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('Enter id of the note: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + 'Enter positive integer!' + Style.RESET_ALL)