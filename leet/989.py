class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = str(k)
        n = len(s)
        m = len(num)
        answer = []
        i, j, carry = n-1,m-1, 0 
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0: 
                add = int(s[i]) + num[j] + carry
            elif j >= 0: 
                add = num[j] + carry
            elif i >= 0:
                add = int(s[i]) + carry
            if add >= 10:
                carry = add // 10
                answer.append(add%10)
            else:
                answer.append(add)
                carry = 0
            i -= 1
            j -= 1
        if carry > 0: answer.append(carry)
        return answer[::-1]
       
