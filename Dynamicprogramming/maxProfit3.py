# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = [[0,0,0] for i in range(0, len(prices))]
        sell = [[0,0,0] for i in range(0, len(prices))]
        buy[0][0] = -prices[0]
        sell[0][0] = 0

        for i in range(1, 2 + 1):
            buy[0][i] = float('-inf')
            sell[0][i] = float('-inf')
        
        for i in range(1, len(prices)):
            buy[i][0] = max(buy[i-1][0], sell[i-1][0] - prices[i])
            for j in range(1, 3):
                buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j-1] + prices[i])
        
        return max(sell[len(prices)-1])



prices = [1,2,3,4,5]
a = Solution()
print(a.maxProfit(prices))