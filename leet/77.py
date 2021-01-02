from typing import List
import itertools
n = 4
k = 2

def combine(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))
'''
def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def dfs(elements, start: int, k: int):
        # k 개로 이루어진 조합 = 한번 반복시 k 1씩 감소하는 방식으로 k개 확인
        if k == 0:
            result.append(elements.copy())
        # start = 숫자이기 때문에 1 부터 시작 따라서 n 개의 수 = n+1 까지의 수
        for i in range(start, n + 1):
            elements.append(i)
            # 다음 시작 점은 i+1이다. 조합이기 때문에 중복 불가이고 1부터 시작이기 때문에 무조건 1높은 다음 수부터 시작!
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([],1,k)
    return result
'''
print(combine(n,k))