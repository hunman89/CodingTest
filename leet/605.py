class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_F = 0
        range_F = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                range_F += 1
            elif flowerbed[i] == 1:
                if range_F - 1 >= 1: max_F += (range_F - 1) // 2 + (range_F - 1) % 2
                range_F = -1
        
        if range_F >= 1:
            max_F += (range_F) // 2 + (range_F) % 2
        
        return max_F >= n