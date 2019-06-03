class Solution:
    cache = None
    def isMatch(self, s: str, p: str) -> bool:
        self.cache = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return self.match(0, 0, s, p)
    def match(self, i: int, j: int, s: str, p: str) -> bool:
        if self.cache[i][j] is not None:
            return self.cache[i][j] is True
        if j == len(p):
            ans = i == len(s)
        else:
            cur_match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = (self.match(i, j + 2, s, p)) or (cur_match and self.match(i + 1, j, s, p))
            else:
                ans = cur_match and self.match(i+1, j+1, s, p)
        self.cache[i][j] = True if ans else False
        return ans