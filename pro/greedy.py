def solution(n, lost, reserve):
    _lost = [ l for l in lost if l not in reserve ]
    _reserve = [ r for r in reserve if r not in lost ]
    for a in _reserve:
        if a - 1 in _lost:
            _lost.remove(a-1)
        elif a + 1 in _lost:
            _lost.remove(a+1)     
    return n - len(_lost)