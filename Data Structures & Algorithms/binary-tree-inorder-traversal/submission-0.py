# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        stack = []
        c = root
        while c or stack:
            while c:
                stack.append(c)
                c = c.left
            c = stack.pop()
            res.append(c.val)
            c = c.right
        return res