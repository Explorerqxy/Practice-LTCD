# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummynode = ListNode(0)
        cur = head
        while cur:
            temp = cur.next
            pos = dummynode
            while pos.next and pos.next.val < cur.val:
                pos = pos.next
            cur.next = pos.next
            pos.next = cur
            cur = temp
        return dummynode.next

#trick
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        result = []
        while h:
            result.append(h.val)
            h = h.next
        result.sort()
        h = head
        for i in result:
            h.val = i
            h = h.next
        return head