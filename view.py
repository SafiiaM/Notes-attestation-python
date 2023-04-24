from colorama import Fore, Style


class View(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(Fore.YELLOW + '________________________________________________'
                  + Style.RESET_ALL)
            print(note)
            print(Fore.YELLOW + '________________________________________________'
                  + Style.RESET_ALL)

    @staticmethod
    def show_note(note):
        print(Fore.YELLOW + '________________________________________________'
              + Style.RESET_ALL)
        print(note)
        print(Fore.YELLOW + '________________________________________________'
              + Style.RESET_ALL)

    @staticmethod
    def show_empty_list_message():
        print(Fore.YELLOW + '________________________________________________'
              + Style.RESET_ALL)
        print('List of the notes is empty!')
        print(Fore.YELLOW + '________________________________________________'
              + Style.RESET_ALL)

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.RED + '________________________________________________'
              + Style.RESET_ALL)
        print('Note with id: {} is not found!'.format(note_id))
        print(Fore.RED + '________________________________________________'
              + Style.RESET_ALL)

    @staticmethod
    def display_note_id_exist(note_id):
        print(Fore.RED + '________________________________________________')
        print('Note with id: {} already exists!'.format(note_id))
        print('________________________________________________'
              + Style.RESET_ALL)

    @staticmethod
    def display_note_stored():
        print(Fore.YELLOW + '________________________________________________' + Style.RESET_ALL)
        print(Fore.GREEN + 'Note is added successfully!' + Style.RESET_ALL)
        print(Fore.YELLOW + '________________________________________________' + Style.RESET_ALL)

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.YELLOW + '________________________________________________' + Style.RESET_ALL)
        print(Fore.GREEN + 'Note with id:{} is updated successfully!'
              .format(note_id) + Style.RESET_ALL)
        print(Fore.YELLOW + '________________________________________________' + Style.RESET_ALL)

    @staticmethod
    def display_note_deletion(note_id):
        print('--------------------------------------------------------------')
        print(Fore.LIGHTRED_EX + 'Note with id: {} is deleted!'.format(note_id) + Style.RESET_ALL)
        print('--------------------------------------------------------------')

    @staticmethod
    def display_all_notes_deletion():
        print(Fore.RED + '--------------------------------------------------------------')
        print('All the notes are deleted!')
        print('--------------------------------------------------------------' + Style.RESET_ALL)


def display_note_id_not_exist(search_id):
    return search_id
