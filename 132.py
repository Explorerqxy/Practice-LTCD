class Solution:
    def minCut(self, s: str) -> int:
        if not s or s == s[::-1]: return 0
        n = len(s)
        for i in range(n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        g = [i for i in range(-1, n)]
        for i in range(n):
            for k in range(0, min(n - i, i + 1)):
                if s[i + k] != s[i - k]:
                    break
                g[i + k + 1] = min(g[i + k + 1], g[i - k] + 1)
            for k in range(1, min(n - i, i + 2)):
                if s[i + k] != s[i - k + 1]:
                    break
                g[i + k + 1] = min(g[i + k + 1], g[i - k + 1] + 1)
        return g[n]