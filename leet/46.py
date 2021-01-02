from typing import List
import itertools
nums = [1,2,3]

def permute(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))

'''
def permute(nums: List[int]) -> List[List[int]]:
    result = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    
    dfs(nums)
    return result
'''

print (permute(nums))

