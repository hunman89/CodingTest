class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0 and a[i] == '1': s += 1
            if j >= 0 and b[j] == '1': s += 1
            if s == 0:
                answer += "0"
            elif s == 1:
                answer += '1'
                carry = 0
            elif s == 2:
                answer += '0'
                carry = 1
            else:
                answer += '1'
                carry = 1            
            i -= 1
            j -= 1
        return answer[::-1]



        # def toInt(a):
        #     n = len(a)
        #     ans = 0
        #     step = 0
        #     while step < n:
        #         v = a[n - step - 1]
        #         ans +=  int(v) * (2 ** step)
        #         step += 1
        #     return ans

        # return format(toInt(a) + toInt(b), 'b')        