class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        Since integers are not indexable, dun convert to save memory and runtime
        """
        if x < 0:
            return False

        reversed_num = 0
        temp = x
        while temp != 0 :
            digit = temp % 10 # get last digit
            reversed_num = reversed_num * 10 + digit # add last digit to reversed number
            temp = temp // 10 # remove last digit of analysis to continue iterating
        # loop has finished, now compare reversed and x
        if x == reversed_num:
            return True
        return False


solution = Solution()
assert(solution.isPalindrome(121))