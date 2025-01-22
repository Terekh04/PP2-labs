fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#adds certain elements from one list to another

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#same

#newlist = [expression for item in iterable if condition == True]

newlist = ['hello' for x in fruits]
#set 'hello' instead of every element in the list