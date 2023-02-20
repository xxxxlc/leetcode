# 给你两个 二维 整数数组 nums1 和 nums2.

# nums1[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
# nums2[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
# 每个数组都包含 互不相同 的 id ，并按 id 以 递增 顺序排列。

# 请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：

# 只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。
# 每个 id 在结果数组中 只能出现一次 ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则认为其对应的值等于 0 。
# 返回结果数组。返回的数组需要按 id 以递增顺序排列。

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []

        i = 0
        j = 0
        
        while(j < len(nums2) and i < len(nums1)):
            if nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i = i + 1
            elif nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            else:
                res.append(nums2[j])
                j += 1
        
        if j < len(nums2):
            for k in range(j, len(nums2)):
                res.append(nums2[k])

        if i < len(nums1):
            for k in range(i, len(nums1)):
                res.append(nums1[k])
        
        return res
        


nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]


a = Solution()
print(a.mergeArrays(nums1, nums2))