# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        c = root
        while c or stack:
            if c:
                res.append(c.val)
                stack.append(c.right)
                c = c.left
            else:
                c = stack.pop()
        return res