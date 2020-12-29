# ListNode 구현 안함

def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
        return  None
    
    odd = head
    even = even_head = head.next
    
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    odd.next = even_head
    return head
