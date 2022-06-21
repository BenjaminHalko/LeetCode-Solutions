# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        check = head
        
        while check != None:
            while check.next != None and check.next.val == check.val:
                check.next = check.next.next
            check = check.next
            
        return head