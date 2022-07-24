# 给你一个整数数组 ranks 和一个字符数组 suit 。你有 5 张扑克牌，第 i 张牌大小为 ranks[i] ，花色为 suits[i] 。

# 下述是从好到坏你可能持有的 手牌类型 ：

# "Flush"：同花，五张相同花色的扑克牌。
# "Three of a Kind"：三条，有 3 张大小相同的扑克牌。
# "Pair"：对子，两张大小一样的扑克牌。
# "High Card"：高牌，五张大小互不相同的扑克牌。
# 请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型 。

# 注意：返回的字符串 大小写 需与题目描述相同。


class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """

        card = {}
        suit = {}

        for i in range(len(ranks)):
            card[ranks[i]] = card.get(ranks[i], 0) + 1
            suit[suits[i]] = suit.get(suits[i], 0) + 1
        
        if len(suit.keys()) == 1:
            return "Flush"
        
        for key, value in card.items():
            if value >= 3:
                return "Three of a Kind"
        
        for key, value in card.items():
            if value == 2:
                return "Pair"
        
        return "High Card"

ranks = [8,10,2,12,9]
suits = ["a","b","c","a","d"]

a = Solution()
print(a.bestHand(ranks, suits))