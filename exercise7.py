filenames = ["a.txt","b.txt","c.txt"]
for item in filenames:
    file = open(f"files/{item}",'r')
    text = file.read()
    print(text)
    file.close()