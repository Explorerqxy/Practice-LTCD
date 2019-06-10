class Solution:
    def uniquePathwithObstacles(self, obsgrid):
        obs = obsgrid
        m = len(obs)
        n = len(obs[0])
        for i in range(m):
            for j in range(n):
                if obs[i][j] == 1:
                    obs[i][j] = 0
                else:
                    if j != 0 and i != 0:
                        obs[i][j] = obs[i-1][j] + obs[i][j-1]
                    elif i == 0 and j == 0 :
                        obs[i][j] = 1
                    elif i == 0 and obs[i][j-1] == 1:
                        obs[i][j] = 1
                    elif j == 0 and obs[i-1][j] == 1:
                        obs[i][j] = 1
        return obs[i][j]
    
