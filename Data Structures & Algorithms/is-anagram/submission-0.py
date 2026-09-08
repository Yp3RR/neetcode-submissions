class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p = {}
        q = {}
        if len(s) != len(t):
            return False

        for c1,c2 in zip(s,t):
            if c1 not in p:
                p[c1] = 1
            else :
                p[c1] += 1

            if c2 not in q:
                q[c2] = 1
            else:
                q[c2] += 1

        if p!=q:
            return False
        return True