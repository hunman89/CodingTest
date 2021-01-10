class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            print(node)
            if node:
                print(node.left)
                print(node.right)
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
                
        return root