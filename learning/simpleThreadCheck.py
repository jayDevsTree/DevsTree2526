import threading
import time

print(threading.current_thread())
print(threading.current_thread().is_alive())



def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

def print_letters():
    for ch in 'abcde':
        print("Letter:", ch)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print("Done")
