s = ["h","e","l","l","o"]
s.reverse

'''
left,right = 0, len(s)-1
while left <= right:
  s[right], s[left] =  s[left], s[right]
  right -= 1
  left += 1

print(s)
'''