class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        i = 0
        char = ""
        num = 0
        for c in chars:
            if c == char:
                num += 1            
            else:
                if num > 1:
                    for j in str(num):
                        chars[i] = j
                        i += 1
                chars[i] = c
                char = c
                i += 1
                num = 1        
        if num > 1:
            for j in str(num):
                chars[i] = j
                i += 1
        return i