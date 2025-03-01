def square(n): 
    i=1
    while i < n:
        yield i**2 
        i+=1
    
m = int(input())

for num in square(m): 
    print (num)