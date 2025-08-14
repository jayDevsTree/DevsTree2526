import threading    
import time

videos = ["1.mp4","2.mp4","3.mp4","4.mp4","5.mp4"]

class myClass(threading.Thread):
    def __init__(self,val):
        print("MyClass constructor called...")
        threading.Thread.__init__(self)
        self.suitable_kid = val
        
    def run (self):
        if self.suitable_kid:
            print("Suitable for kids")
        for vid in videos:
            print(f'{vid} is uploading...')
            time.sleep(1)
            print(f'{vid} is sent.')
            
t1 = myClass(True)
t1.start()


for i in range (5):
   time.sleep(1)
   print("Checking Copyrights...")
            
        
