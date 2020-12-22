def solution(arr):
  def merge(arr):
    answer = []
    amount = 0
    for i in range(len(arr)):
      if i > 0:
        if arr[i] == arr[i-1]:
          amount += 1
        else:
          amount += 1
          answer.append(amount)
          amount = 0    
    answer.append(amount+1)
    return answer

  n = 0
  while arr != [1]:
    arr = merge(arr)
    n += 1
  return n
