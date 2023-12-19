waiting_list = ["prince","apeksha","krishiv","Eliza"]
waiting = []
for item in waiting_list:
    waiting.append(item.capitalize())

waiting.sort()

for index,item in enumerate(waiting):
    print(f"{index+1}.{item.capitalize()}")
