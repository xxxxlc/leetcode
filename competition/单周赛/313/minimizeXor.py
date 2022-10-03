# 给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：

# x 的置位数和 num2 相同，且
# x XOR num1 的值 最小
# 注意 XOR 是按位异或运算。

# 返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。

# 整数的 置位数 是其二进制表示中 1 的数目。


class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        cnt = 0
        exist = [False] * 35

        while(num2 > 0):
            if (num2 & 1):
                cnt += 1
                num2 /= 2
        
        ans = 0
        x = 0
        for i in range(30, -1, -1):
            if (num1 >> i) & 1:
                exist[i] = True
            if exist[i]:
                if cnt > 0:
                    cnt -= 1
                    x += (1<<i)
                else:
                    ans += (1 << i)


num1 = 3
num2 = 5

a = Solution()
print(a.minimizeXor(num1, num2))