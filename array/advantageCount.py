# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。

# 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。

class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        ans = [0] * n

        idx1, idx2 = list(range(n)), list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])

        left, right = 0, n - 1

        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1
        
        return ans
            

                

nums1 = [12,24,8,32]
nums2 = [13,25,32,11]

a = Solution()
print(a.advantageCount(nums1, nums2))