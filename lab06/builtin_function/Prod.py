import math

def multiply(a):
    return math.prod(a)

a = []
while True:
    b = input("Input a number: ")
    if b == "":  
        break
    try:
        a.append(float(b))  
    except ValueError:
        print("It's not a number.")

result=multiply(a)
print(result)