nums = [-1,0,1,2,-1,-4]
# 투 포인터 필수!
# 정렬을 한 뒤, 중복값을 확인한다.
nums.sort()

# 정답의 형식
result = []

# 3포인터 -> 1포인터 탐색 + 2포인터 탐색
for i in range(len(nums)-2):
  # 중복 확인
  if i > 0 and nums[i] == nums[i-1]:
    continue

  left, right = i+1, len(nums)-1
  while left < right:
    sum = nums[i] + nums[left] + nums[right]

    # 포인터 이동! 정렬 되있기 때문에 작으면 left를 오른쪽 크면 반대 
    if sum < 0:
      left += 1
    elif sum > 0:
      right -= 1
    else:
      result.append((nums[i], nums[left], nums[right]))
      # 같은 값 스킵
      while left < right and nums[left] == nums[left + 1]:
        left += 1
      while left < right and nums[right] == nums[right - 1]:
        right -= 1
      # 다음 포인터로 = 합이 0인 것을 찾기 때문에 둘다 움직여야 한다.
      left += 1
      right -= 1
print(result)