T = [73, 74, 75, 71, 69, 72, 76, 73]

def dailyTemperatures(T):
  # 0으로 초기화
  answer = [0] * len(T)    
  stack = []
  for i, cur in enumerate(T):
    # stack에 값이 있고, 그 인덱스에 해당하는 온도가 현재 온도보다 작다 = 온도가 올라갔다.
    while stack and cur > T[stack[-1]]:
      # stack에서 값을 빼고, 인덱스 차이를 통해 얼마만에 올라갔는지 입력
      last = stack.pop()
      answer[last] = i - last
    stack.append(i)
      
  return answer

print(dailyTemperatures(T))


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            next_t = temperatures[i]
            while len(stack) > 0 and stack[-1][-1] < next_t:
                index, value = stack.pop()
                answer[index] = i - index
            stack.append((i,temperatures[i]))
        return answer