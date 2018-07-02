from datetime import datetime
from datetime import timedelta
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(60)
        #time.sleep(1) #for testing
        t -= 1
count = 0
now = datetime.now()
nowPlus25 = now + timedelta(minutes = 25)

nowMinute = now.minute
nowPlus25Min = nowPlus25.minute

while count <= 4:
    while (nowMinute != nowPlus25Min):
        print("Break time will be at: " + str(nowPlus25))
        countdown(25)
        time.sleep(1)
        now = datetime.now()
        nowMinute = now.minute
        # if nowMinute == nowPlus25Min:
        #     break

    print("Take a break!")

    now = datetime.now()
    nowPlusFive = now + timedelta(minutes = 5)
    nowPlusFiveMin = nowPlusFive.minute

    while (nowMinute != nowPlusFiveMin):
        print("Work timer will start at: " + str(nowPlusFive))
        countdown(5)
        time.sleep(1)
        now = datetime.now()
        nowMinute = now.minute
    count += 1
