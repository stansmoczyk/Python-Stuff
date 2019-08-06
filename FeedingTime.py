import time
import webbrowser
#Program runs after timer ends
total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(14400)
    #starts and runs every 3 hours at 14400 seconds
    webbrowser.open("http://www.youtube.com/watch?v=YXw16RzMofo")
    break_count = break_count + 1