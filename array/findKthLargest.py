# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        k = len(nums) - k
        while(lo < hi):
            p = self.partition(nums, lo, hi)
            print(nums)
            if p < k:
                lo = p + 1
            elif p > k:
                hi = p - 1
            else:
                return nums[p]

        return -1            
    
    def partition(self, nums, lo, hi):
        if lo == hi:
            return lo
        
        pivot = nums[lo]
        i = lo + 1
        j = hi 
        while(True):
            while(nums[i] < pivot):
                i = i + 1
                if i >= hi:
                    break
            while(nums[j] > pivot):

                j = j - 1
                if j <= lo:
                    break
            if i >= j:
                break
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
        
        temp = nums[lo]
        nums[lo] = nums[j]
        nums[j] = temp

        return j


nums = [3,2,1,5,6,4]
k = 2
a = Solution()
print(a.findKthLargest(nums, k))
    

