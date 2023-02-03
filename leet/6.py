def convert(self, s: str, numRows: int) -> str:   
    if numRows == 1: return s
        
    rows = ["" for i in range(numRows)]
    
    i = 0
    j = 0
    direct = True
    
    while i < len(s):
        rows[j] += s[i]
        i += 1
        if j == numRows - 1:
            direct = False
        if j == 0:
            direct = True
        if direct:
            j += 1
        else:
            j -= 1
    return "".join(rows)

    # cycle = numRows*2 -2
    # if cycle == 0:
    #     return s
    
    # strings = []
    
    # for i in range(numRows):
    #     strings.append("")
    
    # for i in range(len(s)):
    #     k = i % cycle
    #     if k < numRows:
    #         strings[k] += s[i]
    #     else:
    #         strings[numRows*2 - 2 - k] += s[i]
    # return "".join(strings)