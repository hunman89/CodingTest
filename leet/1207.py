class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #counter
        occ = Counter(arr)
        keys = occ.keys()
        values = occ.values()
        set_values = set(values)
        return len(keys) == len(set_values)
            
        
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         occ = {}
#         for i in arr:
#             if i in occ:
#                 occ[i] += 1 
#             else:
#                 occ[i] = 1
#         return len(occ.values()) == len(set(occ.values()))
            