from functions import load_file, write_todos, print_todos
import time

input_prompt = "Enter your to do item: "
choice_prompt = "Type Add, View, Edit, Done or Exit: "
view_msg = "Your To-Do list: "
edit_prompt = "Type the item number you want to edit: "
new_item_prompt = "Enter your new to do: "
index_err = "Incorrect Item number. Please enter item number from below list:"
done_prompt = "Type the item to be marked as done: "
value_error = "Your command is not valid. Please input a todo number from below list:"
command_err = "Invalid command. Please try again."

print(time.strftime("Date: %dth %b, %Y"))
todos = load_file()
while True:
    user_choice = input(choice_prompt)
    match user_choice.upper().strip():
        case 'ADD':
            todo = input(input_prompt) + "\n"
            todos.append(todo.capitalize())
            todos.sort()
            write_todos(todos)

        case 'VIEW':
            print_todos(todos, view_msg)

        case 'EDIT':
            print_todos(todos, view_msg)

            try:
                item_num = int(input(edit_prompt).strip())-1
            except ValueError:
                print_todos(todos, value_error)
                continue

            if item_num > len(todos) or item_num < 0:
                print_todos(todos, index_err)
                continue
            else:
                new_item = input(new_item_prompt).capitalize()
                todos[item_num] = new_item + "\n"
                todos.sort()
                write_todos(todos)
                print_todos(todos, view_msg)
        case 'DONE':
            print_todos(todos, view_msg)

            try:
                completed_item = int(input(done_prompt).strip())-1
            except ValueError:
                print_todos(todos, value_error)
                continue

            if completed_item > len(todos) or completed_item < 0:
                print_todos(todos, index_err)
                continue
            else:
                todos.pop(completed_item)
                todos.sort()
                write_todos(todos)
                print_todos(todos, view_msg)
        case 'EXIT':
            print("Exiting!")
            break
        case _:
            print(command_err)
            continue