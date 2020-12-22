import re
list = []
s = "A man, a plan, a canal: Panama"
s = s.lower()
s = re.sub('[^0-9a-z]','',s)

print(s == s[::-1])
