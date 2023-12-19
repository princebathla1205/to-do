date = input("Enter today's date: ")
mood = input("Rate your mood from 1 to 10: ")
thought = input("How was your day today? ")

with open(f"journal/{date}.txt",'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thought)