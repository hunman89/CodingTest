nums = [1,2,3,4]
# 왼쪽의 곱에다가 오른쪽의 곱을 곱한다
# 순서대로 하면서 (왼쪽은 왼쪽부터 오른쪽은 오른쪽부터) 곱한 값을 재사용 할 수 있게 한다. 

answer = []
multi = 1
for i in range(len(nums)):
  answer.append(multi)
  multi *= nums[i]

multi = 1
for i in range(len(nums)-1, 0 - 1,-1):
  answer[i] *= multi
  multi *= nums[i]
print(answer)