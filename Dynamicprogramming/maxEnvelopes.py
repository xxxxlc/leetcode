# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

# 注意：不允许旋转信封。


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # for i in range(0, len(envelopes)):
        #     for j in range(0, i):
        #         if envelopes[i][0] < envelopes[j][0]:
        #             temp = envelopes[i]
        #             envelopes[i] = envelopes[j]
        #             envelopes[j] = temp
        #         elif envelopes[i][0] == envelopes[j][0]:
        #             if envelopes[i][1] > envelopes[j][1]:
        #                 temp = envelopes[i]
        #                 envelopes[i] = envelopes[j]
        #                 envelopes[j] = temp

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(0, i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)




envelopes = [[1,1],[1,1],[1,1]]
a = Solution()
print(a.maxEnvelopes(envelopes))