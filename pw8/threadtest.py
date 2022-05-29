import threading
import time
import pickle

from domains.Student import Student


class BackgroundThread(threading.Thread):
    def __init__(self, sleepTime):
        threading.Thread.__init__(self)
        self.__sleepTime = sleepTime

    def run(self):
        for i in range(self.__sleepTime):
            time.sleep(1)
            print(f"iterate #{i}")
        print(f"Finished sleeping {self.__sleepTime}s")


backgroundThread0 = BackgroundThread(10)
backgroundThread0.start()    # note no args here
backgroundThread0.join()

for i in range(5):
    time.sleep(1)
    print(f"Main: iterate #{i}")

print("Finished main thread")
