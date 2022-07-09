# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = tail = None
        temp = head
        
        while head:
            if head.next == None or head.next.val != temp.val:
                if temp.next and temp.next.val == temp.val:
                    temp = head = head.next
                else:
                    if result == None: result = temp
                    else: tail.next = temp
                    tail, temp = head, head.next
                    head = head.next
                    tail.next = None
            else: head = head.next
                
        return result