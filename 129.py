# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self,root):
        self.ret = []
        self.inorder(root,0)
        return sum(self.ret)
    def inorder(self, node, val):
        if node:
            val = val * 10 + node.val
            if node.left is  None and node.right is None:
                self.ret.append(val)
            if node.left :
                self.inorder(node.left, val)
            if node.right:
                self.inorder(node.right, val)