class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        try:
            m = len(grid)
            n = len(grid[0])
        except:
            return 0

        # -------------------------DFS 开始------------------------
        # 定义dfs递归方程
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and int(grid[i][j]):
                grid[i][j] = '0'
                for a, b in ((1, 0), (0, -1), (-1, 0), (0, 1)):
                    dfs(i + a, j + b)

        # ---------------------------------------------------------

        r = 0
        for i in range(m):
            for j in range(n):
                r += int(grid[i][j])
                dfs(i, j)  # 调用dfs沉没一整块陆地
        return r


#W2

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        res = 0
        # 遍历每一个字符
        for i in range(n):
            for j in range(m):
                # 如果遍历字符是陆地"1"
                if grid[i][j] == "1":
                    res += 1
                    # 递归查找与这块陆地相连的所有陆地 并将他们改为零
                    self.change(grid, i, j)
        return res

    def change(self, grid, i, j):
        grid[i][j] = "0"
        # 判断上方字符
        if i > 0 and grid[i - 1][j] == "1":
            self.change(grid, i - 1, j)
        # 判断左方字符
        if j > 0 and grid[i][j - 1] == "1":
            self.change(grid, i, j - 1)
        # 判断下方字符
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            self.change(grid, i + 1, j)
        # 判断右方字符
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            self.change(grid, i, j + 1)