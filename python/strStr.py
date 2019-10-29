# 10/28/2019
# Implement strStr() - https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        
        n = len(haystack)
        start = 0
        end = len(needle)
        
        while end <= n:
            if haystack[start:end] == needle:
                return start
            start += 1
            end += 1
        return -1

if __name__ == '__main__':
    solution = Solution()

    cases = (
        ("hello", "ll"),
        ("aaaaa", "aab"),
        ("a", "a"),
        ("a", ""),
        ("", "a")
    )

    for haystack, needle in cases:
        answer = solution.strStr(haystack, needle)
        print(answer)