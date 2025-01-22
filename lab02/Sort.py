thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#just sorting by alphabet

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#same with numbers

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#sorted in reverse

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#You can also customize your own function by using the keyword argument key = function
#The function will return a number that will be used to sort the list (the lowest number first):
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#sorting starting from lowercase
