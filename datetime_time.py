
from datetime import datetime, date

time_now = datetime.now

print(time_now().strftime("%Y/%m/%d"))

today_date = date.today()
print(today_date)