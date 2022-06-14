# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rootList = []
        while head != None:
            rootList.append(head)
            head = head.next
        
        return rootList[int(len(rootList)/2)]