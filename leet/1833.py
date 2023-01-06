class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        answer = 0
        while costs and coins - costs[-1] >= 0:
            coins = coins-costs.pop()
            answer += 1
        return answer