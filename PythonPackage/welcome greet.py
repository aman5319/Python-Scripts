import datetime
import os

currentTime = datetime.datetime.now()
currentTime = currentTime.hour

if 6 <= currentTime <= 12:
    message = "Good Morning"
elif 13 <= currentTime <= 16:
    message = "Good Afternoon"
elif 17 <= currentTime <= 19:
    message = "Good Evening"
else :
    message="It's Night"

input1 = open("abc.txt", "w");
input1.write(message + " AmiDezCod")
input1.close()

os.system("festival --tts abc.txt")
input1 = open("abc.txt", "w")
input1.write("Ubuntu" + str(" Welcomes you"))
input1.close()
os.system("festival --tts abc.txt")
