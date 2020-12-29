def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        node, prev = next, node
        
    return prev