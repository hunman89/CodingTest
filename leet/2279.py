class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        answer, remains = 0, []

        for i in range(len(capacity)):
            remain = capacity[i] - rocks[i]
            if remain == 0:
                answer += 1
            else:
                remains.append(remain)
        
        remains.sort(reverse=True)
        
        while remains and remains[-1] <= additionalRocks:
            additionalRocks -= remains.pop()
            answer += 1
        return answer
