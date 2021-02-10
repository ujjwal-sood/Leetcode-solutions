class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        h1=[0]*26
        h2=[0]*26
        for x in range(len(s1)):
            h1[ord(s1[x])-ord('a')]+=1
            h2[ord(s2[x])-ord('a')]+=1
        for j in range(0,len(s2)-len(s1)):
            if self.match(h1,h2):
                return True
            h2[ord(s2[j+len(s1)])-ord('a')]+=1
            h2[ord(s2[j])-ord('a')]-=1
        return self.match(h1,h2)
            
    def match(self,h1,h2):
        for i in range(len(h1)):
            if h1[i]!=h2[i]:
                return False
        return True