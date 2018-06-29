from datetime import datetime
from datetime import timedelta
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(60)
        t -= 1

now = datetime.now()
nowPlusOne = now + timedelta(minutes = 25)

nowMinute = now.minute
nowPlusOneMin = nowPlusOne.minute

while (nowMinute != nowPlusOneMin):
        time.sleep(1)
        now = datetime.now()
        nowMinute = now.minute
        print("Break time will be at: " + str(nowPlusOne))
        countdown(25)



print("Take a break!")

