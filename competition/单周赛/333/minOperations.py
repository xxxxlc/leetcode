# 给你一个正整数 n ，你可以执行下述操作 任意 次：

# n 加上或减去 2 的某个 幂
# 返回使 n 等于 0 需要执行的 最少 操作数。

# 如果 x == 2i 且其中 i >= 0 ，则数字 x 是 2 的幂。

class Solution:
    def minOperations(self, n: int) -> int:
        
        n = bin(n)[2:]

        ans = 0

        i = len(n) - 1


        while(i >= 0):
            if n[i] == '1':
                j = i - 1
                while(j >= 0 and n[j] == '1'):
                    j -= 1

                if i - j > 1:
                    if j == -1:
                        n = '1' + '0' * (i - j) + n[i+1:]
                    else:
                        n = n[:j] + '1' + '0' * (i - j) + n[i+1:]
                    ans += 1
                i = j
            else:
                i -= 1
        
        return ans + n.count('1')
    






n = 39

a = Solution()
print(a.minOperations(n))