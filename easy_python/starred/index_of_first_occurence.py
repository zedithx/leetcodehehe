class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+n]:
                return i
        return -1