import datetime  
today = datetime.datetime.now()  
yesterday = datetime.datetime(today.year, today.month, today.day) - datetime.timedelta(1)  
tomorrow = datetime.datetime(today.year, today.month, today.day) + datetime.timedelta(1)  

print(f"Yesterday's date: {yesterday.strftime("%Y-%m-%d")}")  
print(f"Today's date: {today.strftime("%Y-%m-%d")}")  
print(f"Tomorrow's date: {tomorrow.strftime("%Y-%m-%d")}")  
