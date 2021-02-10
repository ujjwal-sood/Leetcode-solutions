class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h=[0]*26
        i,res=0,0
        for j in range(len(s)):
            h[ord(s[j])-ord('A')]+=1
            while not self.check(h,k):
                h[ord(s[i])-ord('A')]-=1
                i+=1
            res=max(res,j-i+1)
        return res         
        
    def check(self,h,k):
        s=sum(h)
        m=max(h)
        if s-m>k:
            return False
        return True