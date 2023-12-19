import random

lb = int(input("Enter Lower bound: "))
ub = int(input("Enter Upper bound: "))

randnum = random.randint(lb, ub)
print("Random number between",lb,ub,"is",randnum)