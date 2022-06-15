# 如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 等差数列 。
# 更正式地，数列 s 是等差数列，只需要满足：对于每个有效的 i ， s[i+1] - s[i] == s[1] - s[0] 都成立。

# 例如，下面这些都是 等差数列 ：

# 给你一个由 n 个整数组成的数组 nums，和两个由 m 个整数组成的数组 l 和 r，后两个数组表示 m 组范围查询，
# 其中第 i 个查询对应范围 [l[i], r[i]] 。所有数组的下标都是 从 0 开始 的。

# 返回 boolean 元素构成的答案列表 answer 。如果子数组 nums[l[i]], nums[l[i]+1], ... , nums[r[i]] 
# 可以 重新排列 形成 等差数列 ，answer[i] 的值就是 true；否则answer[i] 的值就是 false 。



class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        ans = []
        for i in range(len(l)):
            ans.append(self.isArithmectic(nums[l[i]:r[i]+1]))
        return ans

    def isArithmectic(self, nums):
        if len(nums) < 2:
            return False
        if len(nums) == 2:
            return True
        nums = sorted(nums)
        diff = nums[1] - nums[0]

        for i in range(1, len(nums) - 1):
            if nums[i + 1] - nums[i] != diff:
                return False
        
        return True



nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]

a = Solution()
print(a.checkArithmeticSubarrays(nums, l, r))
