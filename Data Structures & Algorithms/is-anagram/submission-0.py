class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        for i in s :
            if i in d_s :
                d_s[i] += 1
            else :
                d_s[i] = 1
        d_t = {}
        for i in t :
            if i in d_t :
                d_t[i] += 1
            else :
                d_t[i] = 1
        if d_t == d_s :
            return True
        return False
        