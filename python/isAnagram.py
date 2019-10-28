# 10/28/1029
# Valid Anagram - https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.memoryEfficientSolution(s, t)

    # Even though this solution used a table, the size remains
    #   constant, so we only use O(1) space
    def memoryEfficientSolution(self, s, t):
      ref = "abcdefghijklmnopqrstuvwxyz"
      hash_table = [0] * 26

      for i in s:
         hash_table[ref.index(i)] += 1
      
      for i in t:
          hash_table[ref.index(i)] -= 1
          if hash_table[ref.index(i)] < 0:
             return False
      
      return True
        
    
    # This was my initial solution, but uses O(2*n) space
    def initialSolution(self, s, t):
        s_map = dict()
        t_map = dict()
        
        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1
        
        for i in t:
            if i in t_map:
                t_map[i] += 1
            else:
                t_map[i] = 1
        
        return s_map == t_map

if __name__ == '__main__':
    solution = Solution()

    cases = (
        ("anagram", "nagaram"),
        ("rat", "car")
    )

    for s, t in cases:
        answer = solution.isAnagram(s, t)
        print(answer)