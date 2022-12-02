class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = Counter(word1), Counter(word2)
        s1, s2 = Counter(w1.values()), Counter(w2.values())
        
        set1, set2 = set(word1), set(word2)
        
        return ((set1 == set2) and (s1 == s2))