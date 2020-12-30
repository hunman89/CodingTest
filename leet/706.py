import collections
# 개별 체이닝 방식을 위해 listNode구현
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        # defaultdict의 특징은 없는 index를 조회하면 default를 만든다는 것이다. 따라서 index를 바로 조회하지 않고 value를 조회한다.
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        # index에 값들이(listNode)있다면, 시작부터 하나하나 보면서 key가 있나 보고 값을 교체한다.
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        # 아니면 다음에 연결
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
            

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next