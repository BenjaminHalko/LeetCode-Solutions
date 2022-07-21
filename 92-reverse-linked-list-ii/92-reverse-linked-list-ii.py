# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        root, node, i, startNode, lastNode = head, None, 0, head, head
        while head:
            i += 1
            if i == right:
                startNode.next, head.next = head.next, lastNode
                if not node: return head
                node.next = head
                break
                
            if i < left: node = head
            elif i == left: startNode = lastNode = head
            if i > left: head.next, lastNode, head = lastNode, head, head.next
            else: head = head.next
            
        return root