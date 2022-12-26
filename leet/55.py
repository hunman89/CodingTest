class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n # 끝까지 갈 수있는 possability 저장
        dp[n-1] = True # 당연히 마지막은 True
        for i in range(n-2, -1, -1):  # 마지막 앞에서 부터 하나씩 
            for j in range(i+1, min(n, i+nums[i]+1)): # 그 점의 다음점에서 끝 or 최대 거리까지 순회하면서
                if dp[j]:    # 끝까지 갈 수 있는 점이 하나라도 있으면
                    dp[i] = True # possability 업데이트
                    break # 다음 점 이동
        return dp[0] #첫번째 점에서 가능한지 확인 = 시작이 첫번째니까