class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        reverse = list(reversed(strs))
        start = reverse.pop()
        check = [0] * len(start)
        while reverse:
            tmp = reverse.pop()
            for i,j in enumerate(start):
                if check[i] == 0:
                    if j > tmp[i]:
                        check[i] = 1
            start = tmp
        return sum(check)