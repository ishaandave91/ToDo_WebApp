import streamlit as st
import functions


todos = functions.load_file()


def add_todo():
    new_todo = st.session_state['todo_ipbox'] + '\n'
    todos.append(new_todo)
    todos.sort()
    functions.write_todos(todos)
    st.session_state['todo_ipbox'] = ''
    return


st.title('Todo List:')

for index, todo_item in enumerate(todos):
    checkbox = st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_item]
        st.experimental_rerun()


st.text_input(label='Test', placeholder='Add your ToDo item here...',
              on_change=add_todo, key='todo_ipbox')


st.session_state