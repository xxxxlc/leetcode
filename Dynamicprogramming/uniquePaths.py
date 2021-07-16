# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

# 问总共有多少条不同的路径？


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp = [[0 for i in range(0, n)] for j in range(0, m)]
        # print(dp)
        for i in range(1, n):
            dp[0][i] = 1
        for i in range(1, m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m - 1][n - 1]



m = 3
n = 7
a = Solution()
print(a.uniquePaths(m, n))
