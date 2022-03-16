# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        digits[i] += 1
        while(i >0 and digits[i] >= 10):
            digits[i] -= 10
            i = i - 1
            digits[i] += 1
        
        if i == 0 and digits[i] >= 10:
            digits[i] -= 10
            digits = [1] + digits
        return digits


digits = [9]

a = Solution()
print(a.plusOne(digits))