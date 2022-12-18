# 给你一个正整数数组 skill ，数组长度为 偶数 n ，其中 skill[i] 表示第 i 个玩家的技能点。将所有玩家分成 n / 2 个 2 人团队，使每一个团队的技能点之和 相等 。

# 团队的 化学反应 等于团队中玩家的技能点 乘积 。

# 返回所有团队的 化学反应 之和，如果无法使每个团队的技能点之和相等，则返回 -1 。

from collections import Counter


class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        score = int(sum(skill) / (n / 2))

        if score * (n / 2) != sum(skill):
            return -1

        cnt = Counter(skill)
        ans = 0

        for key, val in cnt.items():
            if key >= score:
                return -1
            if score - key not in cnt:
                return -1

            if cnt[score - key] != cnt[key]:
                return -1

            ans += key * (score - key) * cnt[key] 
        
        return ans // 2
        


skill = [3,2,5,1,3,4]

a = Solution()
print(a.dividePlayers(skill))