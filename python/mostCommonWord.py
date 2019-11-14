# 11/14/19
# Most Common Word - https://leetcode.com/problems/most-common-word/

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count = dict()
        
        ex = "!?',;."
        for i in ex:
            paragraph = paragraph.replace(i, ' ')
        
        words = paragraph.split()
        for word in words:
            lc = word.lower()
            if lc not in banned:
                if lc in count.keys():
                    count[lc] += 1
                else:
                    count[lc] = 1
                    
        ptr = None
        mx = float("-inf")
        for key in count.keys():
            if count[key] > mx:
                ptr = key
                mx = count[key]
        
        return ptr

if __name__ == '__main__':
    solution = Solution()

    cases = (
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]),
        ("a, a, a, a, b,b,b,c, c", ["a"])
    )

    for case in cases:
        answer = solution.mostCommonWord(case[0], case[1])
        print(answer)