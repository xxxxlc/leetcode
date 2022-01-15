# 给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。

# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []

        q = k
        i = 0
        j = 0

        bug = [[0, 0, nums1[0] + nums2[0]]]

        while(q > 0):
            minnodeidx = 0
            for node in range(0, len(bug)):
                if bug[node][2] < bug[minnodeidx][2]:
                    minnodeidx = node
            if not bug:
                break
            cur = bug.pop(minnodeidx)
            ans.append([nums1[cur[0]], nums2[cur[1]]])
            q = q - 1

            if cur[1] + 1 < len(nums2):
                cur_right = [cur[0], cur[1] + 1, nums1[cur[0]] + nums2[cur[1] + 1]]
                if cur_right not in bug:
                    bug.append(cur_right)
            if cur[0] + 1 < len(nums1):
                cur_down =  [cur[0] + 1, cur[1], nums1[cur[0] + 1] + nums2[cur[1]]]
                if cur_down not in bug:
                    bug.append(cur_down)    


        return ans


a = Solution()
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(a.kSmallestPairs(nums1, nums2, k))
