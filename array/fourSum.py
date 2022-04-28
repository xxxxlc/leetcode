# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        ans = []
        nums.sort()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1

                while (c < d):
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s == target:
                        temp = [nums[a], nums[b], nums[c], nums[d]]
                        if temp not in ans:
                            ans.append(temp)
                        c += 1
                        d -= 1
                    elif s < target:
                        c += 1
                    elif s > target:
                        d -= 1
        
        return ans
                



nums = [-1,0,1,2,-1,-4]
target = -1

a = Solution()
print(a.fourSum(nums, target))