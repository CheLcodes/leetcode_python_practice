# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head, nums) -> int:
        set_nums = set(nums)
        res = 0
        while head:
            if head.val in set_nums and (head.next == None or head.next.val not in set_nums):
                res += 1
            head = head.next
        return res