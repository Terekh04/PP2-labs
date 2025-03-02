import re

def task(a):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern,a)

str_1 = str(input("Input string: "))
print(task(str_1))