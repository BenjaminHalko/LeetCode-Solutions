# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return None
        while head != None and head.val == val:
            head = head.next
        check = head
        
        while check != None:
            while check.next != None and check.next.val == val:
                check.next = check.next.next
            check = check.next
            
        return head