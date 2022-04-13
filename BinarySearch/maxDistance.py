# 给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。

# 下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j 且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​

# 返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。

# 一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。

class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        j = 0
        while (i < len(nums1) and j < len(nums2)):
            if i <= j and nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
                continue
            i += 1
            j = max(j, i)
        
        return ans


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

a = Solution()
print(a.maxDistance(nums1, nums2))