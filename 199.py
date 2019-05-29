# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level=[root]
        v=[root.val]
        while True:
            next_level=[]
            for node in level:
                for child_node in (node.left, node.right):
                    if child_node:
                        next_level.append(child_node)
            if not next_level:
                return v
            v.append(next_level[-1].val)
            level=next_level