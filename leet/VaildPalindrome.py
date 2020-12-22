list = []
s = "0p"
lower_s = s.lower()
for alphabet in lower_s:
  if 47< ord(alphabet) <58 or 96< ord(alphabet) < 123:
    list.append(alphabet)
print(list == list[:-1])


'''
import re
list = []
s = "A man, a plan, a canal: Panama"
s = s.lower()
s = re.sub('[^0-9a-z]','',s) #정규표현식

print(s == s[::-1]) #슬라이싱
'''