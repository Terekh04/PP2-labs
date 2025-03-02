def Palindrome(a):
    a = a.replace(" ", "").lower()
    return a == a[::1]

a = str(input("Input a string: "))
if (Palindrome(a)):
    print ("True")
else:
    print("False")