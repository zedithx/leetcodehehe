class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        temp = ""
        res = 0
        for element in s:
            if temp == "":
                temp = element
            else:
                current_value, prev_value = hashmap[element], hashmap[temp]
                if current_value > prev_value:
                    res += current_value - prev_value
                    temp = ""
                else:
                    res += prev_value
                    temp = element
        if temp != "":
            res += hashmap[temp]
        return res


"""model answer i guess"""
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         m = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#
#         ans = 0
#
#         for i in range(len(s)):
#             if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
#                 ans -= m[s[i]]
#             else:
#                 ans += m[s[i]]
#
#         return ans


solution = Solution()
print(solution.romanToInt("III"))
assert(solution.romanToInt("III")) == 3
assert(solution.romanToInt("LVIII")) == 58
assert(solution.romanToInt("MCMXCIV")) == 1994