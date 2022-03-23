# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」 定义为：

# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = {n}
        while (True):
            next = 0
            while (n != 0):
                next += (n % 10) ** 2
                n = n // 10
            if next == 1:
                return True
            
            if next in visited:
                return False
            n = next
            visited.add(next)
n = 2
a = Solution()
print(a.isHappy(n))