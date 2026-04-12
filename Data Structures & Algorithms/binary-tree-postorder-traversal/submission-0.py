# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack =[] 
        c = root
        while c or stack:
            if c:
                res.append(c.val)
                stack.append(c)
                c = c.right
            else:
                c = stack.pop()
                c = c.left
        res.reverse()
        return res