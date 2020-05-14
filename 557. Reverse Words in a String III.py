class Solution(object):
    def reverseWords(self, s):
        a = ''
        wb = ''
        for i in range(len(s)):
            c = s[i]
            if c == ' ':
                # do reverse
                for j in range(len(wb) - 1, -1, -1):
                    a += wb[j]
                wb = ''
                a += ' '
            else:
                wb += c

        #flush
        for j in range(len(wb) - 1, -1, -1):
            a += wb[j]

        return a