# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if node == None: return 0
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)
            # low <= node.vat <= high
            return dfs(node.right) + dfs(node.left) + node.val

        return dfs(root)


        # result = []
        # def dfs(node: TreeNode):
        #     if node != None:
        #         if node.val >= low and node.val <= high:
        #             result.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        
        # dfs(root)
        # return sum(result)