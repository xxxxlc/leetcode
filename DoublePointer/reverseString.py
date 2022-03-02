# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while(left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
        
        return s


s = ["h","e","l","l","o"]

a = Solution()
print(a.reverseString(s))