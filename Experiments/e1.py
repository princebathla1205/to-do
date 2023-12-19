import glob

myfiles = glob.glob("../files/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        if "a.txt" in filepath:
            print(file.read())