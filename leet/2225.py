from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_check = defaultdict(int)
        for match in matches:
            lose_check[match[0]] += 0
            lose_check[match[1]] += 1
        result1 = []
        result2 = []
        for key, value in lose_check.items():
            if value == 0:
                result1.append(key)
            if value == 1:
                result2.append(key)
        result1.sort()
        result2.sort()

        return [result1, result2]