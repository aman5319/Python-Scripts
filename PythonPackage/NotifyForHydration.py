import os
import time

os.setuid(os.geteuid())

while True:
    command ="notify-send -i ~/PycharmProjects/PythonHome/j/water.ico " \
              " \"You should Drink water Now and next on $(date -d '+1 hour' '+%T') \" "
    p = os.system('%s' % (command))
    time.sleep(3600)
