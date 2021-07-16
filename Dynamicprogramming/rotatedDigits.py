# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

class Solution(object):
    num_map = dict()
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.num_map:
            return self.num_map[n]
        if n == 0:
            return 0
        s = str(n)
        s1 = ''
        for c in s:
            if c == '1' or c == '0' or c == '8':
                s1 += c
            elif c == '2':
                s1 += '5'
            elif c == '5':
                s1 += '2'
            elif c == '6':
                s1 += '9'
            elif c == '9':
                s1 += '6'
            else:
                return self.rotatedDigits(n - 1)
        
        if int(s1) != n:
            self.num_map[n] = self.rotatedDigits(n - 1) + 1
        else:
            self.num_map[n] =  self.rotatedDigits(n - 1)
        
        return self.num_map[n]



n = 10
a = Solution()
print(a.rotatedDigits(n))
        