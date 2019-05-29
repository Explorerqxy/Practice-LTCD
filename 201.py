class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        str1, str2 = bin(m)[2:], bin(n)[2:]
        length = len(str2)
        if len(str1) < length:
            return 0
        for i in range(length):
            if str1[i] != str2[i]:
                break
        else:
            return m
        return int(str2[:i].ljust(length, "0"), 2)