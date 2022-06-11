# 整数的 数组形式  num 是按照从左到右的顺序表示其数字的数组。

# 例如，对于 num = 1321 ，数组形式是 [1,3,2,1] 。
# 给定 num ，整数的 数组形式 ，和整数 k ，返回 整数 num + k 的 数组形式 。

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = k
        for i in range(len(num) - 1, -1, -1):
            d = num[i] + c
            num[i] = d % 10
            c = d // 10

            if i == 0 and c != 0:
                while (c != 0):
                    num = [c % 10] + num
                    c = c// 10 

        return num




num = [2,1,5]
k = 80666

a = Solution()
print(a.addToArrayForm(num, k))
