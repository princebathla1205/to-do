file = open("../bear.txt")
row = file.readlines()
print(row)
for item in row:
    print(item)
file.close()