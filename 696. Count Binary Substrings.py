class Solution(object):
    def countBinarySubstrings(self, s):

        count = 0
        for i in range(len(s) - 1):
            li = i
            l = s[li]
            ri = i + 1
            r = s[ri]

            if not l == r:

                count += 1
                li -= 1
                ri += 1
                while (li > -1) and (ri < len(s)):
                    if s[li] == s[i] and s[ri] == s[i + 1]:
                        print(li, ri)
                        count += 1
                        li -= 1
                        ri += 1
                    else:
                        break

            else:
                continue

        return count