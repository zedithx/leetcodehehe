class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        array_size = len(nums)
        for i in range(array_size):
            complement = target - nums[i]
            if complement in hash_table:
                return [i, hash_table[complement]]
            else:
                hash_table[nums[i]] = i


solution = Solution()
assert(solution.twoSum([2,7,11,15], 9)) == [1, 0]
assert(solution.twoSum([3,2,4], 6)) == [2, 1]
assert(solution.twoSum([3,3], 6)) == [1, 0]