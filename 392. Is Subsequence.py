"""
pretty basic, but worth practice, covered: while loop, conditions, edge cases
"""
class Solution(object):
    def isSubsequence(self, s, t):

        if len(s) == 0:
            return True
        i, j = 0, 0

        while i < len(s) and j < len(t):
            x = s[i]
            y = t[j]

            if x == y:
                if i == len(s) - 1:
                    return True
                else:
                    i += 1
            j += 1

        return False