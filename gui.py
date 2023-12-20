import PySimpleGUI as sg

label=sg.Text("Enter your todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My app', layout = [[label],[input_box,add_button]])
window.read()
print("Hello")
window.close()