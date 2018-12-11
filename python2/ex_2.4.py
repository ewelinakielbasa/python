import numpy as np
from matplotlib import pyplot as plt
import cmath
import queue
import time
import datetime
import threading

q = queue.Queue()

def makeHistogram(file):
    with open(file) as f:
        data = f.read().split()
    data = list(map(int, data))
    binsNumber = int((len(data)) ** (1 / 2))
    rangeHist = max(data) - min(data)
    width = (rangeHist /binsNumber)

    bins = []
    for i in range(binsNumber + 1):
        bins.append(min(data) + i * width)

    dict = {'data': data, 'bins': bins}
    return dict


class threadHist(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.file = file
    def run(self):
        dict=makeHistogram(self.file)
        q.put(dict)


threadHist('dataHist.txt').start()
threadHist('dataHist2.txt').start()
threadHist('dataHist3.txt').start()

dict1 = q.get()
dict2 = q.get()
dict3 = q.get()
plt.figure(1)                # the first figure
plt.subplot(311)             # the first subplot in the first figure
plt.hist(dict1['data'], dict2['bins'])
plt.subplot(312)             # the second subplot in the first figure
plt.hist(dict2['data'], dict2['bins'])
plt.subplot(313)             # the second subplot in the first figure
plt.hist(dict3['data'], dict3['bins'])
plt.show()

