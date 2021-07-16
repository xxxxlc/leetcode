# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = nums + nums
        res = [0]*len(nums)
        print(nums)
        s = []
        for i in range(len(nums) - 1, -1, -1):
            # print(s)
            while(len(s) > 0 and s[len(s) - 1] <= nums[i]):
                s.pop(len(s)-1)
            if len(s) == 0:
                res[i] = -1
            else:
                res[i] = s[len(s) - 1]

            
            s.append(nums[i])
        
        return res[0:int(len(nums)/2)]

        

nums = [1,2,1]

a = Solution()
print(a.nextGreaterElements(nums))