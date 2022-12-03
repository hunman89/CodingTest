class Solution:
    def frequencySort(self, s: str) -> str:
        sort_dic = sorted(Counter(s).items(), key= lambda item: item[1], reverse=True)
        answer = [char*time for char, time in sort_dic]
        return ''.join(answer)