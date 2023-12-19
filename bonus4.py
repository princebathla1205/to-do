filenames = ["1.Raw data.txt","2.Data mining.py","3.Constant.sy"]

print("filenames are: ", filenames)
i = 0
for filename in filenames:
    filename = filename.replace('.','-',1)
    filenames[i] = filename
    i = i + 1

print("Changed filenames: ", filenames)