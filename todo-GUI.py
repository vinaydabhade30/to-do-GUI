import function_mod
import PySimpleGUI as sg

label = sg.Text("Type in to-do list")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# create the window
window = sg.Window("To-do List", layout=[[label], [input_box, add_button]])
window.read()
window.close()
