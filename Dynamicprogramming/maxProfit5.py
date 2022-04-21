# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

# 返回获得利润的最大值。

# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = [0] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)

        buy[0] = -prices[0] - fee
        sell[0] = float('-inf')

        for i in range(1, len(prices) + 1):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i - 1] - fee)

            if i == 1:
                sell[i] = 0
            else:
                sell[i] = max(sell[i - 1], buy[i - 1] + prices[i - 1])
        
        return sell[len(prices)]




prices = [1, 3, 2, 8, 4, 9]
fee = 2

a = Solution()
print(a.maxProfit(prices, fee))