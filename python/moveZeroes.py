# 10/25/2019
# 283. Move Zeroes - https://leetcode.com/problems/move-zeroes/

# Runtime: O(n) - fast is always moving
# Space: O(1) - only constant variables
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        
        slow = 0
        fast = 1

        while fast != n:
            if nums[slow] == 0 and nums[fast] != 0:
                temp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = temp
            if nums[slow] != 0:
                slow += 1   
            fast += 1
        return nums

if __name__ == '__main__':
    cases = (
        [0, 1, 0, 3, 12],
        [1, 2, 3, 0, 0],
        [1],
        [],
        [1, 0, 1, 1, 1],
        [4,2,4,0,0,3,0,5,1,0]
    )

    solution = Solution()
    for case in cases:
        answer = solution.moveZeroes(case)
        print(answer)

