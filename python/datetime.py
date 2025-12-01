import datetime as dt
current_time='5:55 PM'

current_time=dt.datetime.strptime(current_time,"%I:%M %p")
print(current_time.time())