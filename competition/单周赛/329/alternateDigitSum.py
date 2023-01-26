# 给你一个正整数 n 。n 中的每一位数字都会按下述规则分配一个符号：

# 最高有效位 上的数字分配到 正 号。
# 剩余每位上数字的符号都与其相邻数字相反。
# 返回所有数字及其对应符号的和。

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        nums = str(n)

        ans = 0

        for i, c in enumerate(nums):
            if i % 2 == 0:
                ans += int(c)
            else:
                ans -= int(c)
        
        return ans


n = 521

a = Solution()
print(a.alternateDigitSum(n))