import PySimpleGUI as sg
import functions

label=sg.Text("Enter your todo")
input_box = sg.InputText(tooltip="Enter todo",key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(functions.get_todos(),key='items',enable_events=True,size=(40,15))
edit_button = sg.Button("Edit")

comp_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My app', layout = [[label],[input_box,add_button],
                                       [list_box,edit_button,comp_button],
                                       [exit_button]],
                   font=('Helvetica',20))
print(window['items'])
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['items'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)
        case "Edit":
            todo_to_edit = values['items'][0]
            updated_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = updated_todo + "\n"
            functions.write_todos(todos)
            window['items'].update(values=todos)
        case "items":
            window['todo'].update(value=values['items'][0])
        case "Complete":
            todo_complete = values['items'][0]
            todos = functions.get_todos()
            index = todos.index(todo_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window['items'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()