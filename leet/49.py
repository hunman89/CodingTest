import collections

strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = collections.defaultdict(list) # append시 key값이 없을때 발생하는 keyError를 막아준다
for str in strs:
  anagrams[''.join(sorted(str))].append(str) # list[key].append(value)
print(anagrams.values()) # value값만 모아준다.