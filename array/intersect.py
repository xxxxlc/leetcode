# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        element1 = collections.Counter(nums1)
        element2 = collections.Counter(nums2)
        ans = []
        for key, value in element1.items():
            if key in element2:
                ans.extend(key for _ in range(min(element1[key], element2[key])))
        
        return ans

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

a = Solution()
print(a.intersect(nums1, nums2))