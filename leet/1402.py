class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        answer = 0
        satisfaction.sort()
        if satisfaction[-1] <= 0: return 0
        while satisfaction[0] < 0 and sum(satisfaction) < 0:
                satisfaction.pop(0)
        for i,v in enumerate(satisfaction):
            answer += (i+1)*v
        return answer