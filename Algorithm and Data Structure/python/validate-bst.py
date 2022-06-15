# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        inorder_root = self.inorderBT(root)

        for i in range(1, len(inorder_root)):
            if inorder_root[i] <= inorder_root[i-1]:
                return False
        return True

    def inorderBT(self, root) -> list:
        if root == None:
            return []                     
        inorder = []                       
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        return inorder

a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(7)
f = TreeNode(6)
g = TreeNode(8)

a.left, a.right = b, c
c.left, c.right = f, g

solution = Solution()
print(solution.isValidBST(a))