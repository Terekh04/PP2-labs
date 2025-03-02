import re

def task(a):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', a).lower()

b=input('Input string: ')
print(task(b))