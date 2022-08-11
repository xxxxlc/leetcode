# 累加数 是一个字符串，组成它的数字可以形成累加序列。

# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

# 说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        allZeros = all(i == '0' for i in num)
        if allZeros:
            return True
        
        if num[0] == '0':
            for j in range(2, min(len(num) - 2, len(num) // 2 + 1) + 2):
                num2 = int(num[1:j])

                if self.isAddArray(num, j, 0, num2):
                    return True
        else:

            for i in range(1, len(num) // 2 + 1):
                num1 = int(num[:i])
                if num[i] == '0':
                    num2 = 0
                    if self.isAddArray(num, i + 1, num1, num2):
                            return True
                else:
                    for j in range(i + 1, min(len(num) - 2 * i, len(num) // 2 + 1) + i + 1):
                        num2 = int(num[i:j])

                        if self.isAddArray(num, j, num1, num2):
                            return True
        return False

    
    def isAddArray(self, num, idx, num1, num2):
        if num[idx] == '0':
            return False
        
        k = idx + 1
        while(k <= len(num)):
            num3 = self.transform(num[idx:k])

            if num3 > num2 + num1:
                break

            if num1 + num2 == num3:
                if k == len(num):
                    return True
                num1 = num2
                num2 = num3
                idx = k
            k += 1

        return False

    def transform(self, s):
        return 0 if s[0] == '0' else int(s)


num = "121224036"

a = Solution()
print(a.isAdditiveNumber(num))

