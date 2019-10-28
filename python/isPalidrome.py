# 10/28/2019
# Valid Palindrome - https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        include = '1234567890abcdefghijklmnopqrstuvwxyz'
        s = s.lower()
        first = 0
        last = len(s) - 1
        
        while first < last:
            if s[first] not in include:
                first += 1
                continue
            if s[last] not in include:
                last -= 1
                continue
            if s[first] != s[last]:
                return False
            first += 1
            last -= 1
        return True

if __name__ == '__main__':
    solution = Solution()

    cases = (
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "a"
    )

    for case in cases:
        answer = solution.isPalindrome(case)
        print(answer)