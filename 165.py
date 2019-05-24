class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        while v1 and int(v1[-1]) == 0:
            v1.pop()
        while v2 and int(v2[-1]) == 0:
            v2.pop()
        l1 = len(v1)
        l2 = len(v2)
        if l1 == 0 and l2:
            return -1
        elif l2 == 0 and l1:
            return 1
        elif l1 == 0 and l2 == 0:
            return 0
        t = min(l1, l2)
        for i in range(t):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        if len(v1) == len(v2):
            return 0
        elif len(v1)>len(v2):
            return 1
        else:
            return -1


