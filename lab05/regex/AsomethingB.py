import re

def task(a):
    pattern = r"^a.*b$"
    return re.fullmatch(pattern,a)

str_1 = str(input("Input string: "))
print(task(str_1))