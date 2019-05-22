"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        copied = dict()   # 新建字典（哈希表）
        node = head
        while node is not None:                  # 先复制链表的值
            node_copy = Node(node.val, None, None)
            copied[node] = node_copy
            node = node.next

        node = head
        while node is not None:                  # 再分别复制链表的next和random
            if node.next is None:
                copied[node].next = None
            else:
                copied[node].next = copied[node.next]
            if node.random is None:
                copied[node].random = None
            else:
                copied[node].random = copied[node.random]
            node = node.next

        return copied[head]