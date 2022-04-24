# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给你一个整数，将其转为罗马数字。


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        thousand = num // 1000
        ans += "M" * thousand

        num = num % 1000

        hundred = num // 100
        if hundred <= 3:
            ans += "C" * hundred
        elif hundred == 4:
            ans += "CD"
        elif hundred == 5:
            ans += "D"
        elif 5 < hundred < 9: 
            ans += "D" + "C" * (hundred - 5)
        else:
            ans += "CM"
        
        num = num % 100
        ten = num // 10
        if ten <= 3:
            ans += "X" * ten
        elif ten == 4:
            ans += "XL"
        elif ten == 5:
            ans += "L"
        elif 5 < ten < 9: 
            ans += "L" + "X" * (ten - 5)
        else:
            ans += "XC"
        
        one = num % 10
        if one <= 3:
            ans += "I" * one
        elif one == 4:
            ans += "IV"
        elif one == 5:
            ans += "V"
        elif 5 < one < 9: 
            ans += "V" + "I" * (one - 5)
        else:
            ans += "IX"

        return ans
num = 11

a = Solution()
print(a.intToRoman(num))