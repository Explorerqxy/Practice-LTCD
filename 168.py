class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        10进制转码26进制

        """
        if n == 1:
            return "A"
        p = n
        r = ""
        while p > 0:
            p -= 1  # 此处重要！从0开始计数 0-A 1-B
            r = chr(p % 26 + 65) + r
            p /= 26
        return r

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<=26: return chr(n+64)
        if n%26 == 0:
            right = chr(90)
            left = int(n/26)-1
        else:
            right = chr(n%26+64)
            left = int(n/26)
        return self.convertToTitle(left) + right