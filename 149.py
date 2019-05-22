class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(points)
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)
        res = 0
        for i in range(n):
            lookup = defaultdict(int)
            duplicate = 0
            tmp_max = 0
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0 and y == 0:
                    duplicate += 1
                    continue
                # print(x, y)
                g = gcd(x, y)
                if g != 0:
                    x /= g
                    y /= g
                lookup[(x, y)] += 1
                tmp_max = max(tmp_max, lookup[(x, y)])
            res = max(res, tmp_max + duplicate+1)
        return res