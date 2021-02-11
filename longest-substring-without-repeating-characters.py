class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #MY SOLUTION
        """ 
        i,res=0,0
        h={}
        for j in range(len(s)):
            if s[j] not in h:
                h[s[j]]=1
            else:
                h[s[j]]+=1
            while len(h)!=(j-i+1):
                if h[s[i]]>1:
                    h[s[i]]-=1
                else:
                    del h[s[i]]
                i+=1
            res=max(res,j-i+1)
        return res
        """
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength