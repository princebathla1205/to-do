message = ("Enter a todo ")
todos = []
i = 0
while i < 3:
    todo = input(message)
    i = i + 1
    todos.append(todo.upper())
    print(todos)