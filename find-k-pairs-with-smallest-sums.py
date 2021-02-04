class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #(My Solution)
        """
        import heapq
        heap=[]
        l=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(heap)==k:
                    heapq.heappush(heap,(-(nums1[i]+nums2[j]),i,j))
                    heapq.heappop(heap)
                else:
                    heapq.heappush(heap,(-(nums1[i]+nums2[j]),i,j))
                
        for i in range(len(heap)):
            s,p,q=heapq.heappop(heap)
            l.append([nums1[p],nums2[q]])
        return l
        """
        #(OPTIMIZED ONE)
        """
        import heapq
        ret = []
        if len(nums1) * len(nums2) > 0:
            queue = [(nums1[0] + nums2[0], (0, 0))]
            visited = {}
            while len(ret) < k and queue:
                _, (i, j) = heapq.heappop(queue)
                ret.append((nums1[i], nums2[j]))
                if j + 1 < len(nums2) and (i, j + 1) not in visited:
                        heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                        visited[(i, j + 1)] = 1
                if i + 1 < len(nums1) and (i + 1, j) not in visited:
                        heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                        visited[(i + 1, j)] = 1
        return ret
        """

        #(Fastest one)
        import heapq
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs