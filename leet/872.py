# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root:
                if root.left:
                    yield from dfs(root.left)
                if root.right:
                    yield from dfs(root.right)
                if not root.left and not root.right:
                    yield root.val
        
        return list(dfs(root1)) == list(dfs(root2))

        # seq1 = []
        # seq2 = []
        
        # def dfs(root, seq):
        #     if root.left:
        #         dfs(root.left, seq)
        #     if root.right:
        #         dfs(root.right, seq)
        #     if not root.left and not root.right:
        #         return seq.append(root.val)
        
        # dfs(root1, seq1)
        # dfs(root2, seq2)
        # return seq1 == seq2