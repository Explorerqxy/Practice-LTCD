class Solution:
    def solve(self, board):
        def fill(x,y):
            if x < 0 or x > m-1 or y<0 or y > n-1 or board[x][y]!= 'O': return
            queue.append((x,y))
            board[x][y] = 'D'
        def bfs(x,y):
            if board[x][y] == 'O':
                fill(x,y)
            while queue:
                i, j = queue.pop(0)
                fill(i-1,j)
                fill(i+1,j)
                fill(i,j+1)
                fill(i,j-1)
        if len(board) == 0: return
        m = len(board)
        n = len(board[0])
        queue = []
        for j in range(n):
            bfs(0,j)
            bfs(m-1,j)
        for i in range(1,m-1):
            bfs(i,0)
            bfs(i,n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
