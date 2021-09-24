import heapq
class MaxStack:

    def __init__(self):
        self.stack = [] # x
        self.maxHeap = [] # (-x, -idx)
        self.toPop_stack = set() # to track eles to be removed from stack {idx}
        self.toPop_heap = {} # to track eles to be removed from heap  {x: cnt}

    def push(self, x):
        heapq.heappush(self.maxHeap, (-x, -len(self.stack)))
        self.stack.append(x)
    
    def pop(self):
        # pop stack
        x = self.stack.pop()
        key = (-x, -len(self.stack))
        # update toPop heap
        self.toPop_heap[key] = self.toPop_heap.get(key, 0) + 1
        # clean toPop stack
        self.clean_toPop_stack()
        return x
    
    def top(self):
        return self.stack[-1]

    def peekMax(self):
        self.clean_toPop_heap()
        return -self.maxHeap[0][0]

    def popMax(self):
        # clean toPop heap
        self.clean_toPop_heap()
        x, idx = heapq.heappop(self.maxHeap)
        x, idx = -x, -idx
        # update toPop stack
        self.toPop_stack.add(idx)
        # clean toPop stack
        self.clean_toPop_stack()
        return x

    def clean_toPop_stack(self):
        while self.stack and len(self.stack) - 1 in self.toPop_stack:
            self.toPop_stack.remove(len(self.stack) - 1)
            self.stack.pop()
    
    def clean_toPop_heap(self):
        while self.maxHeap and self.toPop_heap.get(self.maxHeap[0], 0):
            self.toPop_heap[heapq.heappop(self.maxHeap)] -= 1