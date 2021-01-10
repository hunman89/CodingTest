N = 3
facility = [[1,1,1]]

def solution(N, facility):
    if len(facility) == 1:
        return 0
    anwser = []
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i >= j:
                results = []
                for f in facility:
                    result = (abs(i - f[0]) + abs(j - f[1])) * f[2]                
                    results.append(result)            
                anwser.append(max(results))
    return min(anwser)

print(solution(N, facility))