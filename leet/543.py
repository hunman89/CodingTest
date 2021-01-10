class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            # 초기화 : 트릭
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            # 왼쪽 끝에서 부터 오른쪽 끝에서의 거리 갱신 
            self.longest = max(self.longest, left + right + 2)
            # 왼쪽 or 오른쪽의 최대 거리 반환
            return max(left , right) + 1
        
        dfs(root)
        return self.longest