import streamlit as st
import functions


todos = functions.load_file()


def add_todo():
    new_todo = st.session_state['todo_ipbox'] + '\n'
    if len(new_todo)>0:
        todos.append(new_todo)
        todos.sort()
        functions.write_todos(todos)
        st.session_state['todo_ipbox'] = ''
    return


st.title('Watch List:')

for index, todo_item in enumerate(todos):
    checkbox = st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_item]
        st.experimental_rerun()


st.text_input(label='', placeholder='Add movie name here...',
              on_change=add_todo, key='todo_ipbox')
st.button('Add', on_click=add_todo, key='add_btn')