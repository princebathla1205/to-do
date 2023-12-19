# from functions import get_todos,write_todos
import functions
import time
# print(help(get_todos))

now = time.strftime("%b %d, %Y %I:%M:%S %p")
print("Hey, It is",now)
while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos("todos_file.txt")

        todos.append(todo.capitalize())
        functions.write_todos(todos, "todos_file.txt")

    elif user_action.startswith("show"):
        # file = open('todos_file.txt','r')
        # todos = file.readlines()
        # file.close()
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index,item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = int(number) - 1

            todos = functions.get_todos("todos_file.txt")

            print(todos[number])
            new_item = input("Enter the new value: ")
            todos[number] = new_item + '\n'

            functions.write_todos(todos, "todos_file.txt")
        except ValueError:
            print("Your command is not valid!")
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = functions.get_todos("todos_file.txt")

            todo_to_delete = todos[number]
            todos.pop(number)
            functions.write_todos(todos, "todos_file.txt")
            print(f"The item deleted is {todo_to_delete}")
        except IndexError:
            print("Your item number is out of Range!")
            continue
        except ValueError:
            print("Your command is not valid. You have entered the item instead of number")
    elif user_action.startswith("exit"):
        break
    else:
        print("Oops! Wrong command entered. Please try again.")

