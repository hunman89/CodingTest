class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t is "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t is "-":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left - right)
            elif t is "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t is "/":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left / right)
            else:
                stack.append(t)
        return int(stack[0])