# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = [0] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        buy[0] = -prices[0]
        sell[0] = float('-inf')
        for i in range(1, len(prices) + 1):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i-1])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i-1])
        
        return sell[len(prices)]


prices = [7,1,5,3,6,4]
a = Solution()
print(a.maxProfit(prices))