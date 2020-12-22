def solution(nums):
  n = []
  def jump(position,answer):
    move_range = nums[position] 
    position += move_range
    if position >= len(nums):
      n.append(answer)
      return 
    if nums[position] == 0:
      position -= 2*move_range
    answer += 1
    jump(position,answer)  
    
  jump(0,0)
  return n[0]

nums = [4,1,2,3,1,0,5]
print(solution(nums))