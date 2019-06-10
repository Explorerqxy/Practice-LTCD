class Solution:
    def minpathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0 :
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
                elif i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        return dp[-1][-1]