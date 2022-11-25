class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1000000007

        leftToRight = [len(arr)] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                leftToRight[stack.pop()] = i
            stack.append(i)

        rightToLeft = [-1] * len(arr)
        stack = []
        for i in reversed(range(len(arr))):
            while stack and arr[i] < arr[stack[-1]]:
                rightToLeft[stack.pop()] = i
            stack.append(i)

        res = 0
        for idx in range(len(arr)):
            l, r = rightToLeft[idx], leftToRight[idx]
            res += (r-idx) * (idx-l) * arr[idx]
            res %= mod
        
        return res