# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 



class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp = [[0] * (amount + 1)]*(len(coins)+1)
        dp = [[0 for col in range(amount + 1)] for row in range(len(coins)+1)]
        print(dp)
        for i in range(0, len(coins)+1):
            dp[i][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(coins)][amount]

        


amount = 5
coins = [1,2,5]
a = Solution()
print(a.change(amount, coins))