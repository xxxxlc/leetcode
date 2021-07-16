# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            else:
                return 0
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(0, len(obstacleGrid[0]))] for j in range(0, len(obstacleGrid))]

        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]



obstacleGrid = [[0],[0],[0]]
a = Solution()
print(a.uniquePathsWithObstacles(obstacleGrid))
