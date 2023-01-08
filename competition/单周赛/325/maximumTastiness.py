# 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。

# 商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。

# 返回礼盒的 最大 甜蜜度。

class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        l = 0
        r = (price[-1] - price[0]) // (k - 1) + 1

        def check(d: int) -> bool:
            cnt = 1
            x0 = price[0]

            for x in price:
                if x >= x0 + d:
                    cnt += 1
                    x0 = x
            return cnt >= k

        while(l + 1 < r):
            mid = (r + l) // 2

            if check(mid):
                l = mid
            else:
                r = mid
        
        return l






price = [13,5,1,8,21,2]
k = 3

a = Solution()
print(a.maximumTastiness(price, k))