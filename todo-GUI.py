import function_mod
import PySimpleGUI as sg
import time

sg.theme("black")
clock = sg.Text("", key='clock')
label = sg.Text("Type in to-do list")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function_mod.file_open_r(), key='r_list_todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


# create the window
window = sg.Window("To-do List",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("calibre", 20))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event)
    # print(2, value)
    # print(3, value['r_list_todos'])
    match event:
        case 'Add':
            todos = function_mod.file_open_r()
            new_todo = value['todo']+'\n'
            todos.append(new_todo)
            function_mod.file_open_w(todos)
            window['r_list_todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = value["r_list_todos"][0]
                # print(todo_to_edit)
                new_todo = value['todo']
                todos = function_mod.file_open_r()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function_mod.file_open_w(todos)
                window['r_list_todos'].update(values=todos)
                # print(index)
            except IndexError:
                sg.popup("Please select item first", font=('Helvetica', 20))
        case 'r_list_todos':
            window['todo'].update(value=value['r_list_todos'][0])
        case 'Complete':
            try:
                todo_to_complete = value["r_list_todos"][0]
                todos = function_mod.file_open_r()
                todos.remove(todo_to_complete)
                function_mod.file_open_w(todos)
                window['r_list_todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select item first", font=('Helvetica', 20))
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()
