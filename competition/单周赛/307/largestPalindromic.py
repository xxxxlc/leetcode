# 给你一个仅由数字（0 - 9）组成的字符串 num 。

# 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。

# 注意：

# 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
# 数字可以重新排序。

import collections

class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """

        c = collections.Counter(num)
        listc = []
        for key ,value in c.items():
            listc.append((key, value))
        listc = sorted(listc, key=lambda x:int(x[0]))
        single = []
        longestNum = ''
        
        longestNum =  (c['0']) // 2 * '0' + longestNum + (c['0']) // 2 * '0'

        if c['0'] % 2 != 0:
            single.append('0')

        for i in range(len(listc)):
            key = listc[i][0]
            value = listc[i][1]
            if key == '0':
                continue
            if value % 2 != 0:
                if value >= 1:
                    longestNum =  (value) // 2 * key + longestNum + (value) // 2 * key
                single.append(key)
            else:
                longestNum =  (value) // 2 * key + longestNum + (value) // 2 * key

        
        if len(single) != 0:
            maxsingle = '0'
            for num in single:
                if int(num) > int(maxsingle):
                    maxsingle = num
            longestNum = longestNum[:len(longestNum)//2] + maxsingle + longestNum[len(longestNum)//2:]

        i = 0
        while(len(longestNum) > 0 and longestNum[i] == '0'):
            longestNum = longestNum[1:len(longestNum)-1]


        if len(longestNum) > 0:
            return longestNum
        return '0'

num = "282273898509619829360"

a = Solution()
print(a.largestPalindromic(num))