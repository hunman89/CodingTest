def convert(self, s: str, numRows: int) -> str:
    cycle = numRows*2 -2
    if cycle == 0:
        return s
    
    strings = []
    
    for i in range(numRows):
        strings.append("")
    
    for i in range(len(s)):
        k = i % cycle
        if k < numRows:
            strings[k] += s[i]
        else:
            strings[numRows*2 - 2 - k] += s[i]
    return "".join(strings)