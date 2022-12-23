class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 3중 캐시
        #
        # buy[i] : day i에 buy 하였을때의 이익
        # sell[i] : sell 하였을때 이익
        # rest[i] : 거래 안했을때 이익
        # 이 셋의 관계는 각각
        #
        # buy[i] = max(buy[i-1], rest[i-1] - prices[i]) -> sell 없는 이유: 전날 sell 하고 바로 buy 할 수 없다.
        # sell[i] = max(buy[i-1] + prices[i], sell[i-1], rest[i-1]) 
        # rest[i] = max(buy[i-1], rest[i-1], sell[i-1]) 
        # 
        # n = len(prices)
        # buy = [0 for i in range(n)]
        # sell = [0 for i in range(n)]
        # rest = [0 for i in range(n)]
        # buy[0] = -prices[0]
        # sell[0] = 0
        # rest[0] = 0
        # for i in range(1,n):
        #     print(i)
        #     buy[i] = max(buy[i-1], rest[i-1] - prices[i])
        #     sell[i] = max(buy[i-1] + prices[i], sell[i-1], rest[i-1])
        #     rest[i] = max(buy[i-1], rest[i-1], sell[i-1])
        # 
        # return sell[-1]

        # 그런데 buy[i] <= rest[i] <= sell[i] 이기 때문에
        # rest[i] = max(sell[i-1], buy[i-1], rest[i-1]) = max(sell[i-1], rest[i-1]) = sell[i-1] 이렇게 되고
        #
        # buy[i] = max(buy[i-1], sell[i-2] - prices[i]) -> rest[i-1] = sell[i-2]
        # sell[i] = max(buy[i-1] + prices[i], sell[i-1])  -> rest 삭제
        #
        # 그리고 배열을 사용하지 않으면

        sell, prev_sell, buy = 0, 0, -10000

        for i in range(len(prices)):
            prev_buy = buy
            buy = max(prev_buy, prev_sell - prices[i])
            prev_sell = sell
            sell = max(prev_buy + prices[i], prev_sell)
        
        return sell