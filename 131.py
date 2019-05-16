class Solution:
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(len(s)):
            tmp = s[:i + 1]
            if tmp==tmp[::-1]:
                self.dfs(s[i + 1:], path + [tmp], res)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res