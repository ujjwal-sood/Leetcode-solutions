class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        h={}
        i,res=0,0
        for j in range(len(tree)):
            if len(h)<3:
                if tree[j] not in h:
                    h[tree[j]]=1
                else:
                    h[tree[j]]+=1
            while len(h)>2:
                if h[tree[i]]>1:
                    h[tree[i]]-=1
                else:
                    del h[tree[i]]
                i+=1
            res=max(res,j-i+1)
        return res