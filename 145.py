# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res

#非递归
        if not root:
            return []
        hel = [root]
        res = []
        while hel:
            node = hel.pop()
            res.append(node.val)
            if node.left:
                hel.append(node.left)
            if node.right:
                hel.append(node.right)
        return res[::-1]