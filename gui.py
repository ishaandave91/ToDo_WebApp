# add clear all feature
# remove trailing spaces from listbox
# try using tkinter- study pysimplegui also

import functions
import PySimpleGUI as gui
import os

# Create Todos.txt file if doesn't already exist
if not os.path.exists('ToDos.txt'):
    with open('ToDos.txt', 'w') as file:
        pass

gui.theme('GrayGrayGray')

item_select_err = 'Please select an item first.'
label = "Type your todo:"
input_box = gui.InputText(tooltip="Enter ToDo", key='todo_input_box')
add_button = gui.Button('ADD', size=10, bind_return_key=True)
exit_button = gui.Button('Exit')
edit_button = gui.Button('Edit')
done_button = gui.Button('Done')
blank_space = ' '
todos = functions.load_file()
list_box = gui.Listbox(todos,
                       key='edit_todo', enable_events=True,
                       font=('Arial', 10), size=[56, 10], pad=((0, 0), (0, 0)))

col1 = [[input_box, add_button]]
col2 = [[list_box, edit_button, done_button]]

layout = [[gui.Frame(layout=col1, title=label, expand_x=True, expand_y=True)],
          [gui.Frame(layout=col2, title='', expand_x=True, expand_y=True)],
          [exit_button]]

main_window = gui.Window('ToDo App',
                         layout=layout,
                         font=('Arial', 12))

event, values = main_window.read()

while True:
    try:
        match event:
            case 'ADD':
                todo_item = values['todo_input_box'] + '\n'
                if todo_item not in todos:
                    todos.append(blank_space+todo_item.capitalize())
                    todos.sort()
                    functions.write_todos(todos)
                    main_window['edit_todo'].update(values=todos)
                    main_window['todo_input_box'].update('')
            case 'Edit':
                todo_edit_item = values['edit_todo'][0]
                new_todo_item = values['todo_input_box']
                edit_item_index = todos.index(todo_edit_item)
                todos[edit_item_index] = new_todo_item.capitalize() + '\n'
                todos.sort()
                functions.write_todos(todos)
                main_window['edit_todo'].update(values=todos)
                main_window['todo_input_box'].update('')
            case 'edit_todo':
                main_window['todo_input_box'].update(value=values['edit_todo'][0].strip())
            case 'Done':
                todo_done_item = values['edit_todo'][0]
                todos.remove(todo_done_item)
                todos.sort()
                functions.write_todos(todos)
                main_window['edit_todo'].update(values=todos)
                main_window['todo_input_box'].update('')
            case 'Exit':
                break
            case gui.WIN_CLOSED:
                break
    except IndexError:
        gui.popup_ok(item_select_err)
    event, values = main_window.read()

main_window.close()
