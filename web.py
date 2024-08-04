import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write('This app is to increase Your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=' ', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')


# Kiedy podajemy key="new_todo" mamy określony konkretny parametr który przekazujemy.
# Kiedy chcemy mieć key= dynamiczny podajemy nazwe zmiennej w tym przypadku ta zmienną jest todo,
# ponieważ chcemy aby każda pozycja z listy miała swój konkretny key.
