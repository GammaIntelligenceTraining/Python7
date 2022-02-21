import datetime
import json


def save_note(title, content):
    global base
    id_ = str(base['settings']['id_'])
    base['notes'][id_] = [title, content, datetime.datetime.now().timestamp()]
    base['settings']['id_'] += 1
    save_base()


def create_note():
    while True:
        title = input('Please enter title, type "exit" to return to main menu: ')
        if title.lower() == 'exit':
            break
        content = input('Please enter note, type "exit" to return to main menu: ')
        if content.lower() == 'exit':
            break
        if not title and not content:
            print('Please enter title and content.')
            continue
        elif not title and content:
            print('Please enter title.')
            continue
        elif title and not content:
            print('Please enter content.')
            continue
        save_note(title, content)
        print('Note saved')
        break


def view_all_notes():
    try:
        for key in base['notes']:
            print(f'ID - {key} Added: '
                  f'{datetime.datetime.strftime(datetime.datetime.fromtimestamp(base["notes"][key][2]), "%d.%m.%Y %H:%M")}')
            print(base['notes'][key][0])
            print()
            print(base['notes'][key][1])
            print('-' * 20)
    except:
        print('There are no notes.')


def delete_note(note_id):
    del base['notes'][note_id]
    save_base()


def pick_note():

    while True:
        try:
            for key in base['notes']:
                print(f'{key} - {base["notes"][key][0]}')
        except:
            print('There are no notes.')
            break
        else:
            user_choice = input('Please enter note ID: ')
            if user_choice.lower() == 'exit':
                break
            if user_choice in base['notes']:
                delete_note(user_choice)
                print('Note was deleted')
            else:
                print(f'Note with id {user_choice} was not found!')
            break


def fill_base():
    for num in range(1, 6):
        save_note(f'Test {num}', f'This is content of test {num}.')


def save_base():
    with open('database.json', 'w', encoding='utf8') as base_file:
        json.dump(base, base_file, indent=2)


def load_base():
    global base
    with open('database.json', 'r', encoding='utf8') as base_file:
        base = json.load(base_file)
        clear_old_notes()


def clear_old_notes():
    tdelta = datetime.timedelta(days=3)
    delete_list = []
    for key in base['notes']:
        if datetime.datetime.now() - datetime.datetime.fromtimestamp(base['notes'][key][2]) > tdelta:
            delete_list.append(key)
    for key in delete_list:
        delete_note(key)


def main_menu():
    load_base()
    while True:
        user_choice = input('Please choose:\n'
                            '1.View all notes\n'
                            '2.Create note\n'
                            '3.Pick and delete\n'
                            '0.Exit\n'
                            '--> ')
        if user_choice == '1':
            view_all_notes()
        elif user_choice == '2':
            create_note()
        elif user_choice == '3':
            pick_note()
        if user_choice == '0':
            break



base = {}

main_menu()