# Bounded Concurrent Queue

from collections import deque
from threading import Lock, Thread
import threading


class ConcurrentQueue(object):
    def __init__(self):
        self.en = Lock()
        self.de = Lock()
        self.queue = deque()
        self.de.acquire()
    
    def enqueue(self, ele):
        self.en.acquire()
        self.queue.append(ele)
        self.en.release()

        if self.de.locked():
            self.de.release()
        print(f'enqueue size {len(self.queue)}, {threading.get_ident()}')
    
    def dequeue(self):
        self.de.acquire()
        val = self.queue.popleft()
        if len(self.queue):
            self.de.release()
        if self.en.locked():
            self.en.release()
        print(f'dequeue size {len(self.queue)}, {threading.get_ident()}')

        return val

def producer(cq):
    for i in range(10):
        cq.enqueue(i)

def consumer(cq):
    for i in range(10):
        cq.dequeue()

cq = ConcurrentQueue()
t1 = [Thread(target=producer, args=(cq,)) for _ in range(3)]
t2 = [Thread(target=consumer, args=(cq,)) for _ in range(3)]


[t.start() for t in t1]
[t.start() for t in t2]

[t.join() for t in t1]
[t.join() for t in t2]

