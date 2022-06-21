# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        if list1 != None and (list2 == None or list1.val <= list2.val):
            head = list1
            list1 = list1.next
        elif list2 != None:
            head = list2
            list2 = list2.next
        else:
            return head
        tail = head
        
        while list1 != None or list2 != None:
            if list1 != None and (list2 == None or list1.val <= list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        return head