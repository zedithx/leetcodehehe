class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        ans = 0
        while start <= end:
            mid = (start + end)//2
            if mid*mid == x:
                return int(mid)
            elif mid*mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return int(ans)