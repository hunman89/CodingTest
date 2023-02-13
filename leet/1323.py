class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = ((high - low) + 1) // 2
        if high % 2 == 1 and low % 2 == 1:
            return count + 1
        return count