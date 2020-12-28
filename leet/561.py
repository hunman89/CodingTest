nums = [1,4,3,2]

print(sum(sorted(nums)[::2]))

'''
answer = 0

nums.sort()

for i in range(len(nums)):
  if i%2 == 0:
    answer += nums[i]
print(answer)
'''