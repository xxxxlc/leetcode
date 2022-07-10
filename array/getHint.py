# 你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

# 写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：

# 猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛），
# 有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。
# 给你一个秘密数字 secret 和朋友猜测的数字 guess ，请你返回对朋友这次猜测的提示。

# 提示的格式为 "xAyB" ，x 是公牛个数， y 是奶牛个数，A 表示公牛，B 表示奶牛。

# 请注意秘密数字和朋友猜测的数字都可能含有重复数字。

import collections

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        Bulls = 0
        Cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                Bulls += 1

        secretSet = collections.Counter(secret)
        guessSet = collections.Counter(guess)

        for key, val in secretSet.items():
            Cows += min(guessSet.get(key, 0), val)

        return str(Bulls) + 'A' + str(Cows - Bulls) + 'B'


secret = "1807"
guess = "7810"

a = Solution()
print(a.getHint(secret, guess))