# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        newHead = head
        head = head.next
        newHead.next = None
        lastHead = head
        while head != None:
            lastHead = head
            head = head.next
            lastHead.next = newHead
            newHead = lastHead
        return newHead