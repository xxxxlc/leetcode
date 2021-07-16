# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 你可以认为每种硬币的数量是无限的。



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1]*(amount+1)
        dp[0] = 0
        for i in range(0, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]


coins = [1,2,5]
amount = 11
a = Solution()
print(a.coinChange(coins, amount))