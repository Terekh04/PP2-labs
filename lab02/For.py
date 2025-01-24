fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#while is like in c++, but this usage of for is interesting
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#nested loops too long in pyhton