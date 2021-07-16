# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        k = min(k, len(prices)//2)
        buy = [[0]*(k+1)]*len(prices)
        sell = [[0]*(k+1)]*len(prices)
        buy[0][0] = -prices[0]
        sell[0][0] = 0
        for i in range(1, k+1):
            buy[0][i] = float('-inf')/2
            sell[0][i] = float('-inf')/2
        for i in range(1, len(prices)):
            buy[i][0] = max(buy[i -1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k+1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(buy[i - 1][j - 1] + prices[i], sell[i - 1][j])
        return max(sell[len(prices) - 1])



a = Solution()
k = 2
prices = [2,1,4]
print(a.maxProfit(k, prices))
