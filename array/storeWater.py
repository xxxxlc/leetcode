# 给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：

# 升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
# 蓄水：将全部水桶接满水，倒入各自对应的水缸
# 每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

# 注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。


import math


class Solution(object):
    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
        max_vat = max(vat)
        if max_vat == 0:
            return 0
        
        ans = 10001

        for i in range(1, 10001):
            if i >= ans:
                break
            update = 0
            for j in range(len(vat)):
                cur = int(math.ceil(float(vat[j]) / i - bucket[j]))
                print(cur)
                if cur > 0:
                    update += cur
                if update >= ans:
                    break
            ans = min(ans, update + i)
        return ans
        



bucket = [16,29,42,70,42,9]
vat = [89,44,50,90,94,91]

a = Solution()
print(a.storeWater(bucket, vat))