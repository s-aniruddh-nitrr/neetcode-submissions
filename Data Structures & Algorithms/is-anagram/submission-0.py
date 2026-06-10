class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list()
        tlist = list()
        for i in s:
            slist.append(i)
        for j in t:    
            tlist.append(j)
        slist.sort()
        tlist.sort()
        if(slist == tlist):
            return True
        return False
        