# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getKthElement(k, m, n):
            index1, index2 = 0, 0
            while (True):
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k = k - (newIndex1 - index1 + 1)
                    index1 = newIndex1 + 1
                else:
                    k = k - (newIndex2 - index2 + 1)
                    index2 = newIndex2 + 1
        
        m = len(nums1)
        n = len(nums2)
        totallength = m + n

        if totallength % 2 == 0:
            return (getKthElement(totallength // 2, m, n) + getKthElement(totallength // 2 + 1, m, n)) / 2.0
        else:
            return getKthElement(totallength // 2 + 1, m, n)



nums1 = [1,2]
nums2 = [3,4]

a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))