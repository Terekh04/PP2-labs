print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
#OR
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])  #All of them are true

bool(False)
bool(None)
bool(0)
bool("")
bool(())                             #These are all false
bool([])
bool({})


def myFunction() :
  return True

print(myFunction())                  #Bool in functions


