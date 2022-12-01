class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        a,b = s[:half], s[half:]
        
        def check_vowels(s: str) -> int:
            count = 0
            # set 으로 하면 66ms ->35ms
            vowels = set('aeiouAEIOU')

            for c in s:
                if c in vowels:
                    count += 1
            return count
        
        return check_vowels(a) == check_vowels(b)