import datetime
from datetime import datetime, timedelta

dif=int(input("How many days?"))
x = datetime.now()
y = x + timedelta(days=dif)

their_difference = y - x

ans = their_difference.total_seconds()

print (ans)