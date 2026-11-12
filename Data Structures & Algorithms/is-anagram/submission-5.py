class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s1 = "".join(sorted(s))
        # t1 = "".join(sorted(t))
        # if(s1 == t1):
        #     return True
        # else:
        #     return False
        s1 = {}
        t1 = {}
        for chr in s:
            if chr in s1:
                s1[chr] += 1
            else:
                s1[chr] = 1
        for chr in t:
            if chr in t1:
                t1[chr] += 1
            else:
                t1[chr] = 1
        if(s1 == t1):
            return True
        else:
            return False