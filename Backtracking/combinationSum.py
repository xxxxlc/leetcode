# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtracking(k, candidates, target):
            if target == 0:
                c = k[:]
                c.sort()
                if c not in ans:
                    ans.append(c[:])
                return
            
            if target < 0:
                return
            
            for i in candidates:
                k.append(i)
                backtracking(k, candidates, target - i)
                k.pop(-1)
        
        backtracking([], candidates, target)

        return ans




candidates = [2,3,5]
target = 8

a = Solution()
print(a.combinationSum(candidates, target))
