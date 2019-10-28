# 10/27/2019
# First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= badVersion:
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    solution = Solution()

    cases = (
        (5, 4),
        (1, 1),
        (2, 1)
    )

    global badVersion

    for case in cases:
        badVersion = case[1]
        answer = solution.firstBadVersion(case[0])
        print(answer)
        