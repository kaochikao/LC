class Solution(object):
    def canConstruct(self, ransomNote, magazine):


        m_d = {}
        for c in magazine:
            if c in m_d:
                m_d[c] += 1
            else:
                m_d[c] = 1

        r_d = {}
        for c in ransomNote:
            if c in r_d:
                r_d[c] += 1
            else:
                r_d[c] = 1

        for k in r_d:
            if not m_d.get(k):
                return False
            elif r_d[k] > m_d[k]:
                return False

        return True


s = Solution()
a = s.canConstruct(ransomNote = "a", magazine = "b")

print(a)