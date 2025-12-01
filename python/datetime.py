from datetime import datetime
current_time='5:55 PM'

current_time=datetime.strptime(current_time,"%I:%M %p")
print(current_time.time())
