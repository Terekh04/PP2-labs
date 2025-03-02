import math

a = str(input("Input string: "))
upper = 0
lower = 0
for i in a:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1

print("Num of upper: ", upper , "\n","Num of lower: ", lower )