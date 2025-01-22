thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#now "blackcurrant" is instead of "banana"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#same but range

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#inserts new element