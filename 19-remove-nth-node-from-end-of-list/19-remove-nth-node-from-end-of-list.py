# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None: return None
        
        nodes = []
        root = head
        while root != None:
            nodes.append(root)
            root = root.next
        
        if(n == 1): nodes[-2].next = None
        elif n == len(nodes): head = head.next
        else: nodes[-n-1].next = nodes[-n+1]
        
            
        return head