# 11/4/2019
# Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/

# Runtime - O(n + m), Space - O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x = len(nums1) - 1
        
        p1 = m - 1
        p2 = n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[x] = nums1[p1]
                p1 -= 1
            else:
                nums1[x] = nums2[p2]
                p2 -= 1
            x -= 1
        
        if p2 >= 0:
            while p2 >= 0:
                nums1[x] = nums2[p2]
                x -= 1
                p2 -= 1

        print(nums1)

if __name__ == '__main__':
    solution = Solution()

    cases = (
        ([1,2,3,0,0,0], 3, [2,5,6], 3),
        ([1,5,6,0,0,0], 3, [2,3,4], 3)
    )

    for case in cases:
        solution.merge(case[0], case[1], case[2], case[3])