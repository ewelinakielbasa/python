#!/usr/bin/python

import threading
import time
import threading

# without death locka

def food(nr, forks, lock):
    print ("start")
    count = 0

    if ((nr + 1) % 5 > nr):
        forks[nr % 5].acquire()
        time.sleep(5)
        forks[(nr + 1) % 5].acquire()

    else:
        forks[(nr + 1) % 5].acquire()
        time.sleep(5)
        forks[nr % 5].acquire()

    print ("eating")

    if ((nr + 1) % 5 > nr):
        forks[(nr + 1) % 5].release()
        forks[nr % 5].release()
    else:
        forks[nr % 5].release()
        forks[(nr + 1) % 5].release()

    print ("end")


forks = []
for i in range(0, 5):
    forks.append(threading.Lock())
lock = threading.Lock()
threads = []


class myThread(threading.Thread):
    def __init__(self, nr, forks, lock):
        threading.Thread.__init__(self)
        self.forks = forks
        self.nr = nr
        self.lock = lock

    def run(self):
        food(self.nr, self.forks, self.lock)


try:
    thread0 = myThread(0, forks, lock).start()
    thread1 = myThread(1, forks, lock).start()
    thread2 = myThread(2, forks, lock).start()
    thread3 = myThread(3, forks, lock).start()
    thread4 = myThread(4, forks, lock).start()

except:
    print ("Error: unable to start thread")

print ("the end")