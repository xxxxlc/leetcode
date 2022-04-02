# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用 一次 。

import collections

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target:
            return []
        candidates = sorted(collections.Counter(candidates).items())
        self.ans = []

        self.backtrack(0, target, [], candidates)

        return self.ans

    
    def backtrack(self, idx, target, track, candidates):
        if target == 0:
            self.ans.append(track[:])
            return
        if idx == len(candidates) or target < candidates[idx][0]:
            return
        
        self.backtrack(idx + 1, target, track[:], candidates)

        most = min(target // candidates[idx][0], candidates[idx][1])
        
        for i in range(1, most + 1):
            track.append(candidates[idx][0])
            self.backtrack(idx + 1, target - i * candidates[idx][0], track[:], candidates)
        track = track[:-most]


candidates = [2,5,2,1,2]
target = 5

a = Solution()
print(a.combinationSum2(candidates, target))