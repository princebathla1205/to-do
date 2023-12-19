contents = ["hello, My name is "
            "Prince",
            "I have 2 children and only 1 wife",
            "Children names are Eliza and Krishiv"]
filenames = ["hello.txt","data.txt","trailer.txt"]

for content,filename in zip(contents, filenames):
    file = open(f"files/{filename}",'w')
    file.write(content)
    file.close()

print("All done")
