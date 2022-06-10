#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1.val = str(l1.val)
        l2.val = str(l2.val)
        while l1.next != None:
            l1.next.val = str(l1.next.val)+l1.val
            l1 = l1.next
        while l2.next != None:
            l2.next.val = str(l2.next.val)+l2.val
            l2 = l2.next
        x = str(int(l1.val)+int(l2.val))[::-1]
        print(l1.val,l2.val)
        root = ListNode(int(x[0]))
        r = root
        for n in x[1:]:
            r.next = ListNode(int(n))
            r = r.next
        return root

# @lc code=end

