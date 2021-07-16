# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

# 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res_dict = {}
        res1 = []
        s = []
        for i in range(len(nums2) - 1, -1, -1):
            print(s)
            while(len(s) > 0 and s[len(s) - 1] <= nums2[i]):
                s.pop(len(s)-1)
            if len(s) == 0:
                res_dict[nums2[i]] = -1
            else:
                res_dict[nums2[i]] = s[len(s) - 1]

            
            s.append(nums2[i])

        for i in range(0, len(nums1)):
            res1.append(res_dict[nums1[i]])
        return res1

nums1 = [1,3,5,2,4]

nums2 = [6,5,4,3,2,1,7]
a = Solution()
print(a.nextGreaterElement(nums1, nums2))