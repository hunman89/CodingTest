s = "pwwkew"

used = {}

max_length = start = 0
# index는 계속 진행하는 포인터, start는 글자 길이의 시작점
for index, char in enumerate(s):
  if char in used:
    # 한번 나왔던 문자이면, 전에 나왔던 부분에서 + 1 문자부터 시작!
    start = used[char] + 1
  else:
    # 문자 길이 갱신
    max_length = max(max_length, index - start + 1)
  # 문자와 현재위치 삽입.
  used[char] = index

print(max_length)