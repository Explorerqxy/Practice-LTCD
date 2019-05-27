class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        x, y = len(dungeon), len(dungeon[0])
        dp = [[0]*y for _ in range(x)]  # 能到达最后在这个位置的最小体力值,>=1
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for j in range(y-2, -1, -1):  # 最后一行
            dp[-1][j] = max(1, dp[-1][j+1]-dungeon[-1][j])
        for i in range(x-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
        for j in range(y-2, -1, -1):  # 从右到左
            for i in range(x-2, -1, -1):  # 从下到上
                # 找这个位置下边或右边需要的较少体力值
                dp[i][j] = max(1, min(dp[i][j+1], dp[i+1][j])-dungeon[i][j])
        return dp[0][0]