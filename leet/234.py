# ListNode 구현 안함

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()
        
        if not head:
            return True
        
        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 끝까지 탐색하면서
        while fast and fast.next:
            # 2칸 이동
            fast = fast.next.next
            # 연결리스트를 역순으로 만든다.한칸씩 이동하면서 그러면 fast가 끝에 도달했을때 slow는 중간, 역순 연결리스트는 딱 반이다.
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수일경우 가운데는 제외하고 넘어간다.
        if fast:
            slow = slow.next
        # slow가 계속 진행하면서 rev랑 비교한다.
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev