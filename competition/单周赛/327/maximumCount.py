# 给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。

# 换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
# 注意：0 既不是正整数也不是负整数。


class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = len(nums) - 1

        l = 0

        while(l < r):
            mid = l + (r - l) // 2

            if nums[mid] * nums[mid + 1] <= 0:
                if nums[mid] == 0 or nums[mid + 1] == 0:
                    i = mid
                    j = mid + 1
                    while(i >= 0 and nums[i] == 0):
                        i -= 1

                    while(j < len(nums) and nums[j] == 0):
                        j += 1

                    return max(i + 1, len(nums) - j)
                else:
                    return max(mid + 1, len(nums) - mid - 1)
            
            if nums[mid] < 0:
                l = mid + 1
            
            else:
                r = mid
        
        return len(nums)



nums = [-5, -4, -3, -2,-1,0,1,2,3,4]

a = Solution()
print(a.maximumCount(nums))