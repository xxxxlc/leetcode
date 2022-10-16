# 给你一个由 正 整数组成的数组 nums 。

# 你必须取出数组中的每个整数，反转其中每个数位，并将反转后得到的数字添加到数组的末尾。这一操作只针对 nums 中原有的整数执行。

# 返回结果数组中 不同 整数的数目。

class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
            s.add(self.reverse(nums[i]))
        
        return len(s)

    def reverse(self, num):
        s = str(num)[::-1]
        num = int(s)
        return num

nums = [2,2,2]
a = Solution()
print(a.countDistinctIntegers(nums))