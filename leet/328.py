# # ListNode 구현 안함

# def oddEvenList(self, head: ListNode) -> ListNode:
#     if head is None:
#         return  None
    
#     odd = head
#     even = even_head = head.next
    
#     while even and even.next:
#         odd.next, even.next = odd.next.next, even.next.next
#         odd, even = odd.next, even.next
#     odd.next = even_head
#     return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
            
        odd = head
        even = head.next
        eHead = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = eHead
        
        return head