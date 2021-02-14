class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        h=[]
        for x in range(len(points)):
            if len(h)==K:
                heapq.heappush(h,[-(points[x][0]**2+points[x][1]**2),x])
                heapq.heappop(h)
            else:
                heapq.heappush(h,[-(points[x][0]**2+points[x][1]**2),x])
        res=[]
        while h:
            a,b=heapq.heappop(h)
            res.append([points[b][0],points[b][1]])
        return res
        """
        self.sort(points, 0, len(points)-1, K)
        return points[:K]
    
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points, l, p-1, K)
            
    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]                
        return a"""