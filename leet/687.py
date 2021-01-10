class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            # 초기값
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 왼쪽, 오른쪽 값 비교
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0                
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            
            self.result = max(self.result, left + right)
            
            # 왼쪽 오른쪽 중 큰값 리턴.
            return max(left, right)
        
        dfs(root)
        return self.result