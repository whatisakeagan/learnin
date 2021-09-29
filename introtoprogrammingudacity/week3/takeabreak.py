import webbrowser
import time

mxbrks = 3
brk = 0

print ("This program started on"+ time.ctime())
while brk < mxbrks:
	time.sleep(1)
	webbrowser.open("https://youtu.be/Y9Vh8XGgqjE")
	brk +=1
