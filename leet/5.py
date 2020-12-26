s = "cbbd"

if len(s) < 2 and s == s[::-1]:
  print(s)

def expand(left:int, right:int) -> str:
  while left >= 0 and right <= len(s) and s[left]==s[right - 1]:
    left -= 1
    right += 1
  return s[left+1:right-1]  

result = ''
for i in range(len(s)):
  result = max(result, expand(i, i+1), expand(i, i+2),key=len) # 홀수, 짝수 모두 비교

print(result)
