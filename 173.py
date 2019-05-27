# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        self.root = root
        self.index = 0
        self._index = []
        self.for_each(root)

    def for_each(self, root):
        # 中序遍历
        if not root: return
        self.for_each(root.left)
        self._index.append(root.val)
        self.for_each(root.right)

    def next(self):
        """
        @return the next smallest number
        """
        value = self._index[self.index]
        self.index += 1
        return value

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self._index)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = []
        self.inOrder(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.tree:
            return self.tree.pop(0)
        else:
            return None

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.tree:
            return True
        else:
            return False

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.tree.append(root.val)
        self.inOrder(root.right)
        return

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()