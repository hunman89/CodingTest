class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.maxlen = k
        # 앞(p1),뒤(p2): queue이기 때문에 요소가 추가되면 뒤가 이동!
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        # 빈 공간 이면.
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            # 한칸 전진, 원형이기 떄문에 최대값을 넘기면 1부터 시작 = 나눈 나머지
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # 빈공간이 이면.
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        if self.q[self.p1] == None:
            return -1
        else:
            return self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None