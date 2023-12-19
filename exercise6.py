filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for item in filenames:
    file = open(f"files/{item}",'w')
    file.writelines("Hello!\n")
    file.close()