# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        b = []
        while(a != None):
            b.append(a.val)
            a = a.next
        c = head
        b.sort()
        for i in b:
            c.val = i
            c = c.next
        return head