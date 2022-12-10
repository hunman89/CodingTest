# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sum_node(node):
            if not node: return 0
            node_sum = node.val + sum_node(node.left) + sum_node(node.right)
            sums.append(node_sum)
            return node_sum
        
        sums = []
        answers = set()
        sum_node(root)
        root_sum = sums[-1]
        
        for s in sums:
            answers.add(s * (root_sum - s))
        return max(answers) % 1000000007