# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = [0] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        freeze = [0] * (len(prices) + 1)

        buy[0] = -prices[0]
        sell[0] = float('-inf')
        freeze[0] = 0

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], freeze[i - 1] - prices[i])
            sell[i] = buy[i - 1] + prices[i]
            freeze[i] = max(sell[i - 1], freeze[i - 1])
        
        return max(sell[-2], freeze[-2])

        


prices = [1,2,3,0,2]
a = Solution()
print(a.maxProfit(prices))