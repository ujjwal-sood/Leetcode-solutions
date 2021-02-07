class Solution:
    def check(self,s1,e1,s2,e2):
        if e2<s1 or s2>e1:
            return False
        return True
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        if len(intervals)==1:
            return intervals
        start,end=intervals[0][0],intervals[0][1]
        nxt=self.merge(intervals[1:])
        
        i=0
        while i<len(nxt):
            if self.check(start,end,nxt[i][0],nxt[i][1]):
                start=min(start,nxt[i][0])
                end=max(end,nxt[i][1])
                nxt.pop(i)
            else:
                i+=1
                
        nxt.append([start,end])
                
        return nxt"""
        
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return mergeds