
while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo ') + "\n"
            with open('todos_file.txt','r') as file:
                 todos = file.readlines()

            todos.append(todo.capitalize())

            with open('todos_file.txt','w') as file_output:
                file_output.writelines(todos)

        case 'show' | 'display':
            # file = open('todos_file.txt','r')
            # todos = file.readlines()
            # file.close()
            with open('todos_file.txt','r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]
            for index,item in enumerate(todos):
                item = item.title()
                item = item.strip('\n')
                print(f"{index + 1}.{item}")
        case 'edit':
            number = input("Enter the item number to edit: ")
            number = int(number) - 1

            with open('todos_file.txt','r') as file:
                todos = file.readlines()

            print(todos[number])
            new_item = input("Enter the new value: ")
            todos[number] = new_item + '\n'

            with open('todos_file.txt','w') as file_output:
                file_output.writelines(todos)
        case 'complete':
            number = int(input("Enter the item number to complete: "))
            number = number - 1
            with open('todos_file.txt','r') as file:
                todos = file.readlines()
            todo_to_delete = todos[number]
            todos.pop(number)
            with open('todos_file.txt','w') as file_output:
                file_output.writelines(todos)
            print(f"The item deleted is {todo_to_delete}")
        case 'exit':
            break
        case _:
            print("You have entered a wrong input!")