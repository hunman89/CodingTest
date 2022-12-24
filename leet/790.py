class Solution:
    def numTilings(self, n: int) -> int:
        # D(n) = 완전한 정사각형 모양이고, 길이 n 일때 경우의 수
        # T(n) = 하나가 튀어나온 모양이고, 길이가 n일때 경우의 수
        # board 의 시직부터 살펴보면
        # 1. 도미노 타일 세로
        # X*****
        # X*****  D(n-1)과 같다
        # 2. 도미노 타일 가로 
        # XX****  
        # YY****  D(n-2)와 같다
        # 3. 트리미노 타일
        # X****
        # XX***   2 * T(n-1)과 같다.

        # 한칸이 튀어나온 모양일때는 어떤 관계가 있나?
        # 1. 처음에 트리미노 타일이 온다.
        # XX****
        #  X****  D(n-2)와 같다.
        # 2. 처음에 도미노 타일이 온다.
        # XX*** 
        #  ****  T(n-1)과 같다.
        
        if n <= 2:
            return n
        
        cache_d = [0 for i in range(n+1)]
        cache_t = [0 for i in range(n+1)]
        
        cache_d[1] = 1
        cache_d[2] = 2
        
        cache_t[2] = 1
        
        for i in range(3, n+1):
            cache_d[i] = (cache_d[i-1] + cache_d[i-2] + 2 * cache_t[i-1]) % ((10**9) + 7)
            cache_t[i] = (cache_t[i-1] + cache_d[i-2]) % ((10**9) + 7)
        
        return cache_d[n]