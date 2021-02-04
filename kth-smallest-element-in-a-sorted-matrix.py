""" (SOLUTION 1 - Using Heap) (GOOD TIME)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])
        heapq.heapify(arr)
        cur = 0
        ans = None
        while cur < k:
            ans = heapq.heappop(arr)
            cur += 1
        return ans
"""

""" (SOLUTION 2 - Using Heap) (MOST TIME)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        
        heap = []
        
        R, C = len(matrix), len(matrix[0])
        
        # to simulate a maxheap invert the values
        # runs in R*C time and O(R*C) space for storing all elements
        # into the heap
        for r in range(R):
            for c in range(C):
                if len(heap) == k:
                    heapq.heappush(heap, matrix[r][c] * -1)
                    heapq.heappop(heap)
                else:
                    heapq.heappush(heap, matrix[r][c] * -1) 
                    
        return heap[0] * -1
"""
## (SOLUTION 3 - MODIFIED BINARY SEARCH) (LEAST TIME- O(NLOG(N)) )
class Solution:
    def getcount(self,arr,mid):
        i,j,count=len(arr)-1,0,0
        while i>=0 and j<len(arr):
            if arr[i][j]>mid:
                i-=1
            else:
                count=count+i+1
                j+=1
        return count
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        low,high,ans=matrix[0][0],matrix[n-1][n-1],matrix[0][0]
        while low<=high:
            mid=low+(high-low)//2
            if self.getcount(matrix,mid)>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans