def solution(n):  
  answer = 0
  n = n-1
  if n != 0 and n % 4 == 0:  
    quoti = n//4
    answer = (quoti+1)*(quoti+2)*(quoti+3)
  else:  
    k = (n - (n//4)+1)
    answer = k*(k+1)
  return answer

print(solution(4))


nums = [4,1,2,3,1,0,5]
position = 0
answer = 0


def jump(position, answer):
  move_range = nums[position] 
  position += move_range
  if nums[position] == 0:
    position -= 2*move_range
  answer += 1
  