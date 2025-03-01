import datetime  
x = datetime.datetime.now()  
five_days_ago = datetime.datetime(x.year, x.month, x.day) - datetime.timedelta(5)  

print(five_days_ago.strftime("%Y-%m-%d"))  
