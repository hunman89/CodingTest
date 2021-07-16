def triangleNumber(nums: [int]) -> int:
    ans = 0
    nums.sort()
    for i in range(nums):
        if i == 0 :
            continue
        if i == 1 :
            continue
        val = nums[i]
        start = 0
        end = i - 1
        while start < end:
            if nums[start] + nums[end] > val:
                ans += end - start
                end -= 1
            else:
                start += 1
    return ans    

nums = [2,2,3,4]
print(triangleNumber(nums))