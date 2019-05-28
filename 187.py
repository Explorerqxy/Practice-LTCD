class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        d = {}
        tmp = s[:10]
        d[tmp] = 1
        for i in range(n - 10):
            tmp = tmp[1:] + s[10 + i]
            d[tmp] = d.get(tmp, 0) + 1
        res = [k for k, v in d.items() if v > 1]
        return res   