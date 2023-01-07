class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        answer, sum_res = 0,0
        for i in range(len(gas)):
            sum_res += (gas[i] - cost[i])
            if sum_res < 0:
                answer = i+1
                sum_res = 0
        return answer