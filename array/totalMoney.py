# Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。

# 最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。

# 给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        numweek = n // 7
        numday = n % 7

        if numweek == 0:
            total = (1 + numday) * numday / 2
        else:
            total = ((1 + 7) * 7 / 2 + (1 + 7) * 7 / 2 + 7 * (numweek - 1)) * numweek / 2 + \
                    (numweek + numweek + numday + 1) * numday / 2
        return int(total)

a = Solution()
n = 20
print(a.totalMoney(n))
