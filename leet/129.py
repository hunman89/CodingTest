class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        self.dfs(root, 0)
        return self.answer
        
    def dfs(self, node, number):
        if not node.left and not node.right:
            self.answer += number * 10 + node.val
        if node.left:
            self.dfs(node.left, number * 10 + node.val)
        if node.right:
            self.dfs(node.right, number * 10 + node.val)