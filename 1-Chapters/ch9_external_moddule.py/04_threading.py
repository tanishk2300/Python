#Learn how to use multithreading in Python to run multiple threads concurrently. -
# -This can help improve the performance of I/O-bound tasks by executing them in parallel, making your programs more efficient and responsive.
import threading
import time 
 
def worker(num):
    print(f"threading{num}: starting")
    time.sleep(2)#simulate some work 
    print(f"thread {num}: Finishing")

threads=[]
for i in range(3):
    thread =threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()#wait for all threads to finish 
print("all threads completed.")