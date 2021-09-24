# Definition for singly-linked list.
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # push node val into a min heap, pop heap to get the smallest node each time
        head = ListNode(0)
        curr = head
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]
        while heap:
            curVal, curIdx = heapq.heappop(heap)
            curHead = lists[curIdx]
            curNext = curHead.next
            curr.next = curHead
            curHead.next = None
            curr = curHead
            curHead = curNext
            if curHead:
                lists[curIdx] = curHead
                heapq.heappush(heap, (curHead.val, curIdx))
        return head.next

        # [heapq.heappush(heap, (l.val, i)) for i, l in enumerate(lists) if l]
        # while heap:
        #     curVal, curIdx = heapq.heappop(heap)
        #     curHead = lists[curIdx]
        #     curNext = curHead.next
        #     move.next = curHead
        #     curHead.next = None
        #     move = curHead
        #     curHead = curNext
        #     if curHead:
        #         lists[curIdx] = curHead
        #         heapq.heappush(heap, (curHead.val, curIdx))
        # return head.next