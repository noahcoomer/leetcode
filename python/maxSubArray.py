# 10/28/2019
# Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dynamic(nums)


    def dynamic(self, nums):
        n = len(nums)
        max_val = float('-inf')
        for i in range(n):
            max_val = max(max_val, nums[i], nums[i] + max_val)
        
        return max_val

    # Runtime: O(n^2)
    # Space: O(1)
    def bruteForce(self, nums):
        n = len(nums)
        max_val = float('-inf')
        #indices = (None, None)

        for i in range(n):
            for j in range(i, n):
                sub_array = nums[i:j]
                if sum(sub_array) > max_val:
                    max_val = sum(sub_array)
                    #indices = (i, j)
        
        # i, j = indices
        # nums[i:j] is the subArray
        return max_val

if __name__ == '__main__':
    solution = Solution()

    cases = (
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    )

    for case in cases:
        answer = solution.maxSubArray(case)
        print(answer)
        