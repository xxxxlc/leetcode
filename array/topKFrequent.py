# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = dict()
        a = []
        for i in range(0, len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        for key, value in map.items():
            a.append([key, value])
        
        a = sorted(a, key=lambda x : x[1], reverse=True)
        ans = []
        for i in range(0, k):
            ans.append(a[i][0])
        return ans


nums = [1,1,1,2,2,3]
k = 2

a = Solution()
print(a.topKFrequent(nums, k))