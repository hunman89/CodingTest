class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic = Counter(tasks)
        answer = 0
        for v in dic.values():
            if v == 1:
                return -1
            else:
                a, b = divmod(v, 3)
                if b == 0:
                    answer += a
                else:
                    answer += a + 1
        return answer
