import webbrowser

user_input = input("Enter what you want to search: ")
webbrowser.open("https://www.google.com/search?q=" + user_input)