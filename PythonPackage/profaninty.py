from urllib.request import urlopen



def readtext():
    file = open("/home/amidezcod/PycharmProjects/PythonHome/j/abc.txt")
    content_of_file=file.read()
    content_of_file = content_of_file.replace(" ","%20")
    print(content_of_file)
    file.close()
    checkprofinity(content_of_file)

def checkprofinity(content_of_file):
    with urlopen("http://www.wdylike.appspot.com/?q="+content_of_file) as response:
        data = response.read()

    print(data.decode())
readtext()
