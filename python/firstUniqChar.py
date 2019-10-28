# 10/28/2019
# First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import deque

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = deque()
        visited = set()
        
        for i in s:
            if i in visited and i in queue:
                queue.remove(i)
            elif i not in visited:
                queue.append(i)
            visited.add(i)
        
        if queue:
            return s.index(queue.popleft())
        return -1

if __name__ == '__main__':
    solution = Solution()

    cases = (
        "leetcode",
        "loveleetcode",
        "aaaaaaaa"
    )

    for case in cases:
        answer = solution.firstUniqChar(case)
        print(answer)