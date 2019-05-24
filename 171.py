class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in s:
            ans = 26 * ans + (ord(i) - ord('A')) + 1
        return ans


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            j = -1 * (i+1)
            res += (26**i) * (ord(s[j])-64)
        return res