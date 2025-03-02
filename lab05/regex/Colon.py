import re

def task(a):
    ans = re.sub(r'[ ,.]',":",a)
    return ans

b = str(input("Input string: "))
print(task(b))