password = input("Enter password: ")

result = {}

if len(password) > 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
        break

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
        break

result["upper"] = upper
print(result)

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")