# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        
        # l, node = 1, head
        # while node.next != None:
        #     node = node.next
        #     l += 1
        # half = l/2
        # l, node = 1,head
        # while l <= half:
        #     node = node.next
        #     l += 1
        # return node