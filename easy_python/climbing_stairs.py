class Solution:
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr # stores this old current as another variable first
            curr = prev + curr # new current is sum of previous two values
            prev = temp # stores the old current as previous value
        return curr