def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    
    prev.next = head
    
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head
        
        prev.next = b
        # head 가 뒤로갔기 때문에 한칸만 이동
        head = head.next
        prev = prev.next.next
    
    return root.next