def solution(nums):
  n = []
  def jump(position,answer):
    move_range = nums[position] 
    position += move_range
    if position == len(nums):
      n.append(answer)
      return 
    if position > len(nums):
      n.append(-1)
      return
    if nums[position] == 0:
      position -= 2*move_range
    answer += 1
    jump(position,answer)  
    
  jump(0,0)
  return n[0]

nums = [2,1,3,1,5]
print(solution(nums))

'''
visit = [] # 방문 노드
check = [0] * len(nums)
idx = len(nums)-1 # 도착 지점
total = []
def node(idx , visit , total):
    for i, v in enumerate(nums):
        if idx == 0:
            total.append(len(visit))
            return 0
        if idx == i:
            continue

        if abs(idx - i) == nums[i]:
            if check[i] == 1: #이미 방문 사이클 생성 (도달 못함)
                return -1
            else:
                check[i] = 1 # 방문 체크
                visit.append(i)
                result = node(i, visit , total)
                visit.pop() # 빼기
                check[i] = 0 #방문 안한걸로 체크
                if result == 0:
                    return 0
                elif result == -1:
                    return -1

if node(idx, visit, total) == -1:
    return -1
else:
    return min(total))
'''