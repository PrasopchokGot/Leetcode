# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
    
a, b, c, d, e, f = (TreeNode('a'), TreeNode('b'), TreeNode('c'), 
                    TreeNode('d'), TreeNode('e'), TreeNode('f'))

a.left, a.right = (b, c)
b.left, b.right = (d, e)
c.right = f

solution = Solution()
print(solution.inorderTraversal(a))