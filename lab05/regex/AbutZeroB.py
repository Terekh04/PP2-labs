import re
def task(a):
   pattern = r'^ab*$' 
   if re.fullmatch (pattern,a):
    return True
   else: 
    return False

b = str(input("Input string: "))
if task(b):
    print ("True")
else: print ("False")