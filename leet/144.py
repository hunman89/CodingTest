# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val:
                    answer.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return answer



# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         answer = []
#         def dfs(node):
#             if node:
#                 if node.val:
#                     answer.append(node.val)
#                 if node.left:
#                     dfs(node.left)
#                 if node.right:
#                     dfs(node.right)
#         dfs(root)
#         return answer