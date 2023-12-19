feet_inches = input("Enter height in feet and inches: ")

def convert(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3084 + inches * 0.0254
    return meters


height = convert(feet_inches)
print(f"Height is {height} meters")