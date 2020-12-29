def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    if not head or m==n:
        return head

    root = start = ListNode(0)
    root.next = head
    # start 지점(m) 까지 노드 연결
    for _ in range(m-1):
        start = start.next
    end = start.next
    
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    
    return root.next