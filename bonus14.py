from converters14 import convert
import parser14

feet_inches = input("Enter height in feet and inches: ")

parsed = parser14.parse(feet_inches)
height = convert(parsed['feet'], parsed['inches'])
print(f"Height is {height} meters which is {parsed['feet']} feet and {parsed['inches']} inches ")
