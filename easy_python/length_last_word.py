class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = s.strip().split(' ')
        return len(str_list[-1])