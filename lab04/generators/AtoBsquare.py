def square_roots(a, b):
    for i in range(a, b):
        yield i**2

a = int(input("1st number: "))
b = int(input("2nd number: "))

for i in square_roots(a,b):
    print(i)