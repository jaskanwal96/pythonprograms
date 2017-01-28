import webbrowser
import time
i = 0
while i < 3 :
    print("This program started on "+time.ctime());
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=34Na4j8AVgA")
    i = i + 1

