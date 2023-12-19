import csv

with open("Weather.csv",'r') as file:
    text = list(csv.reader(file))

station = input("Enter the station: ")
for row in text[1:]:
    if row[0] == station:
        print("Temperature in",station, "is", row[1],"degree Celsius")

