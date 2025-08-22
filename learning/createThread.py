import threading
import time


def display(n,msg):
    for i in range(n):
        print(msg)
        
t1 = threading.Thread(target = display, args=(10,'Custom Thread'))
t1.start()

for i in range(10):
    print("Main Thread", end="")
    
