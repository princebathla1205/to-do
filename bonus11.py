def get_average():
    with open('files/temperatures.txt','r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(item) for item in values]

    average = sum(values) / len(values)
    return average


average = get_average()
print(average)
