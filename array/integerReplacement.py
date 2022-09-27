# 给定一个正整数 n ，你可以做如下操作：

# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# 返回 n 变为 1 所需的 最小替换次数 。

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = float('inf')
        self.m = set()
        self.trackback(n, 0, [])
        return self.ans
    
    def trackback(self, n, steps, track):
        if n == 1:
            print(track)
            self.ans = min(steps, self.ans)
            return 
        
        if n < 1 :
            return

        self.m.add(n)
        
        if n % 2 == 0:
            self.trackback(n // 2, steps + 1, track[:] + [n])
        else:
            self.trackback(n + 1, steps + 1, track[:] + [n])
            self.trackback(n - 1, steps + 1, track[:] + [n])

n = 1234

a = Solution()
print(a.integerReplacement(n))

