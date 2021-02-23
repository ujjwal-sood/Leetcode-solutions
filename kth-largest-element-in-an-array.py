class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo,hi=0,len(nums)-1
        k=hi-k+1
        while lo<hi:
            p=self.partition(nums,lo,hi)
            if p<k:
                lo=p+1
            elif p>k:
                hi=p-1
            else:
                break
        return nums[k]

        # Faster solution same method just shuffle nums before partition
        """
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
        """
    
    def partition(self,nums,lo,hi):
        p=lo
        i,j=lo,lo+1
        while j<=hi:
            if nums[p]>nums[j]:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
            j+=1
        nums[i],nums[p]=nums[p],nums[i]
        return i