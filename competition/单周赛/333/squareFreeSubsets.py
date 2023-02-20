# 给你一个正整数数组 nums 。

# 如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。

# 无平方因子数 是无法被除 1 之外任何平方数整除的数字。

# 返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 109 + 7 取余的结果。

# nums 的 非空子集 是可以由删除 nums 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。


from typing import List



PRIMES = 2,3,5,7,11,13,17,19,23,29
NSQ_TO_MASK = [0] * 31

for i in range(2, 31):
    for j, p in enumerate(PRIMES):
        if i % p == 0:
            if i % (p * p) == 0:
                NSQ_TO_MASK[i] = -1
                break
            NSQ_TO_MASK[i] |= 1 << j

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        M = 1 << len(PRIMES)

        f = [0] * M
        f[0] = 1

        for x in nums:
            mask = NSQ_TO_MASK[x]

            if mask >= 0:
                for j in range(M-1, mask-1, -1):
                    if (mask | j) == j:
                        f[j] = (f[j] + f[mask ^ j]) % MOD
        
        return (sum(f) - 1) % MOD



nums = [3,4,4,5]

a = Solution()
print(a.squareFreeSubsets(nums))