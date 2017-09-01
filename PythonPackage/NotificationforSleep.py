import os,datetime,time

os.setuid(os.geteuid())

hourHand = datetime.datetime.now().hour
while True:
    if 0 <= hourHand <= 6:
        minuteHand = datetime.datetime.now().minute
        if minuteHand == 30 or minuteHand == 00:
            command = "notify-send -t 0 \"you Need to sleep\n Leave some work for tomorrow\" "
            p = os.system('%s' % (command))
            time.sleep(120)
        else:
            continue
