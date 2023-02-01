class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) <= len(str2):
            s1 = str1
            s2 = str2
        else:
            s1 = str2
            s2 = str1
        
        answer = ""
        
        n = len(s1)
        m = len(s2)
        for i in range(1, n+1):
            if n % i == 0 and s1[:i] * (n // i) == s1:
                if s1[:i] * (m // i) == s2:
                    answer = s1[:i]
                    
        return answer