# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        res = []  

        self.dfs(root, targetSum, res, [])

        return res

    def dfs(self, root, target_sum, res, stack):
        # corner case
        if root == None:
            return []
        
        # Check if final path(at leaf) equal to target sum
        if not root.left and root.right and root.val == target_sum:
            stack.append(root.val)
            self.res.append(stack)

        self.dfs(root.left, target_sum - root.val, res, stack + [root.val])
        self.dfs(root.right, target_sum - root.val, res, stack + [root.val])

solution = Solution()
print(solution.pathSum())