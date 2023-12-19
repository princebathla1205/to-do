feet_inches = input("Enter height in feet and inches: ")


def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3084 + inches * 0.0254
    return float(meters)


parsed = parse(feet_inches)
height = convert(parsed['feet'],parsed['inches'])
print(f"Height is {height} meters which is {parsed['feet']} feet and {parsed['inches']} inches ")