import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

texts = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
# r'' : 역슬래쉬를 문자 그대로 해석하게 해 준다.
# \w : 모든 문자
# ^\w : 문자가 아닌것
# if word not in banned : list comprehension

counts = collections.Counter(texts)
# 빈도수를 세어주는 객체
most = counts.most_common(1)
# 빈도수가 높은 것들중 1번째
print(most[0][0]) # 그것의 이름