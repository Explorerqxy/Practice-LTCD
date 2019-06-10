class Solution:
    def uniquepaths(self, m, n):
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n ==1:
            return 1
        dp = [[1]*m for i in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


