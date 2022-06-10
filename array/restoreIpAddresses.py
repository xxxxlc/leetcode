# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) > 12:
            return []
        
        for c in s:
            if not c.isdigit():
                return []
        
        self.ans = []
        self.trackback(s, "", 0)

        return self.ans
    
    def trackback(self, r, track, times):
    
        if len(r) == 0:
            if times == 4:
                self.ans.append(track[:-1])
            return 
        
        if times > 4:
            return
        
        if r[0] == '0':
            self.trackback(r[1:], track + r[0:1] + ".", times + 1)
        else:
        
            for i in range(3):
                if i == len(r):
                    break
                if int(r[0:i + 1]) > 255:
                    continue
                self.trackback(r[i + 1:], track + r[0:i + 1] + ".", times + 1)

s = "0000"

a = Solution()
print(a.restoreIpAddresses(s))