clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
grouped_clothes = {}
answer =  1

def solution(clothes):
  global answer
  for i in clothes:
    hash(i)  
  counts(grouped_clothes)
  answer -= 1
  print(answer)
  #return answer

def hash(clothe):
  if clothe[1] in grouped_clothes.keys():
    grouped_clothes[clothe[1]] += 1
  else:
    grouped_clothes[clothe[1]] = 1

def counts(grouped_clothes):
  global answer
  for i in grouped_clothes.keys():
    answer *= grouped_clothes[i] + 1

solution(clothes)



#def solution(clothes):
#    clothes_type = {}
#
 #   for c, t in clothes:
  #      if t not in clothes_type:
   #         clothes_type[t] = 2
    #    else:
     #       clothes_type[t] += 1

#    cnt = 1
 #   for num in clothes_type.values():
  #      cnt *= num

   # return cnt - 1

