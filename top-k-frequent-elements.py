class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # MY SOLUTION - T.C. -O(Nlogk) and S.C. -O(N+k) using min heap
        """
        import heapq
        h={}
        for x in nums:
            if x in h:
                h[x]+=1
            else:
                h[x]=1
        l=[]
        for x in h:
            if len(l)==k:
                heapq.heappush(l,[h[x],x])
                heapq.heappop(l)
            else:
                heapq.heappush(l,[h[x],x])
        res=[]
        while l:
            a,b=heapq.heappop(l)
            res.append(b)
        return res
        """
        #FASTER ONE - T.C.- O(N) and S.C. - O(N) using Bucket sort 
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]