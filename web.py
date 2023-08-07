import streamlit as st
import functions

st.title('Todo List:')

todos = functions.load_file()

for todo_item in todos:
    st.checkbox(todo_item.strip('\n'))


st.text_input(label='', placeholder='Add your ToDo item here...')

