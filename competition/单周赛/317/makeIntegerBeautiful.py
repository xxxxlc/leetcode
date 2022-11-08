# 给你两个正整数 n 和 target 。

# 如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。

# 找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。


class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        numbers = list(str(n))
        m = len(numbers)
        diff = -target
        for i in range(m):
            numbers[i] = int(numbers[i])
            diff += numbers[i]
        
        x = 0
        j = m - 1
        c = 1
        while (diff > 0 and j >= 0):
            diff -= numbers[j] - 1
            if numbers[j] == 0:
                c = c * 10
                j = j - 1
                continue
            x += (10 - numbers[j]) * c

            j = j - 1
            c = c * 10
            numbers[j] += 1
        
        return x


        

n = 1
target = 1

a = Solution()
print(a.makeIntegerBeautiful(n, target))