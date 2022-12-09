# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMaxDiff(node, high, low):
            if not node: return high - low
            high = max(high, node.val)
            low = min(low, node.val)
            return max(findMaxDiff(node.left, high, low), findMaxDiff(node.right, high, low))
        
        return findMaxDiff(root, root.val, root.val)