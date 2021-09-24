import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] # for second half
        self.maxHeap = [] # for first half
        self.length = 0

    
    def addNum(self, num: int) -> None:
        self.length += 1
        if self.length == 1:
            heapq.heappush(self.minHeap, num)
            return


        if num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap) + 1:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.maxHeap, -num)
            if len(self.minHeap) < len(self.maxHeap):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                    

    def findMedian(self) -> float:
        if self.length % 2:
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()