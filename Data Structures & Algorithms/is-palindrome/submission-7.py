class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char != " " and char.isalnum():
                res = res + char.lower()
        print("res = " + res)
        start = 0
        end = len(res)-1
        while(start < end):
            if(res[start] != res[end]):
                return False 
            if(res[start] == res[end]):
                start+=1
                end-=1
        print(start,"---", end)
        if(len(res)%2 == 0):
            if(start-1==end):
                return True

        if(start == end):
            return True
        return False
        