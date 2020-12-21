class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandy = max(candies)
        canGreatest = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandy:
                canGreatest.append(True)
            else:
                canGreatest.append(False)
        return canGreatest