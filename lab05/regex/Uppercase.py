import re

def task(a):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern,a)

str_1 = str(input("Input string: "))
print(task(str_1))