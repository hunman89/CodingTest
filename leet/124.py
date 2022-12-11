# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = -math.inf
        # max_sum은 기본적으로 전체 경로를 관통하는
        # 하나의 큰 경로가 어떻게 하면 max를 가질지 계산한다.
        def max_sum(node):
            nonlocal answer
            if not node: return 0
            left_sum, right_sum = max_sum(node.left), max_sum(node.right)
            # max_thru: 왼쪽 경로 vs 오른쪽 경로 vs 여기서 시작
            max_thru = max(node.val + max(left_sum, right_sum), node.val)
            # 지금까지 경로의 최대값 vs 
            # 이 노드 + 왼쪽 자식 + 오른쪽 자식 노드 합 
            answer = max(answer, max_thru , node.val + left_sum + right_sum)
            return max_thru
        max_sum(root)
        return answer
        