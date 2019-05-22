# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        pre = head
        lat = head.next
        while lat is not None and lat.next is not None:
            pre = pre.next
            lat = lat.next.next
        p = pre.next
        pre.next = None

        cur = None
        while p is not None:
            q = p.next
            p.next = cur
            cur = p
            p = q

        pre = head
        while pre is not None and cur is not None:
            tmp = cur.next
            cur.next = pre.next
            pre.next = cur
            pre = pre.next.next
            cur = tmp