class Solution:

    def encode(self, strs: List[str]) -> str:
        ch = "é"
        encodestr = ''
        for i in strs:
            encodestr = encodestr+i+ch
        return encodestr

    def decode(self, s: str) -> List[str]:
        print(s)
        result = list()
        j = 0
        i = 0
        while(i<len(s)):
            print('new for i = ', i)
            while (s[i] != 'é'):
                i+=1
            result.append(s[j:i])
            j=i+1
            i+=1
        return result
