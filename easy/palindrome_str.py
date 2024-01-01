class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        String way but slower
        """
        if x < 0:
            return False

        return str(x) == str(x)[::-1]


solution = Solution()
assert(solution.isPalindrome(121))