# 10/25/2019
# 1. Two Sum - https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hash_table = dict()

        for i in range(n):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            hash_table[target - nums[i]] = i


if __name__ == '__main__':
    case_1 = ([2,  7, 11, 15], 9) # Should return [0, 1]

    solution = Solution()
    answer = solution.twoSum(case_1[0], case_1[1])
    print(answer)
