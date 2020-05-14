class Solution(object):
    def licenseKeyFormatting(self, S, K):

        sb = ''
        counter = 0
        for i in range(len(S) - 1, -1, -1):
            c = S[i].upper()
            if counter == K:
                sb += '-'
                counter = 0

            if c == '-':
                continue
            else:
                sb += c
                counter += 1

        return sb[::-1].strip('-')