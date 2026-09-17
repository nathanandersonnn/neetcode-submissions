class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = {}, {}
        for i in s:
            s1[i] = s1.get(i, 0) + 1
        for j in t:
            if j in s1:
                t1[j] = t1.get(j, 0) + 1
            else:
                return False
        return s1 == t1