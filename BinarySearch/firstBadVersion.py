# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while(left <= right):
            mid = (left + right) // 2

            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            if isBadVersion(mid) == False and isBadVersion(mid + 1) == True:
                return mid + 1
            if isBadVersion(mid) == True:
                right = mid - 1
            if isBadVersion(mid) == False:
                left = mid + 1