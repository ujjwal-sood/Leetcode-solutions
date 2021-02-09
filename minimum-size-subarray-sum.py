class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        asum=0
        l=len(nums)+1
        for j in range(len(nums)):
            asum+=nums[j]
            while asum>=target:
                l=min(l,j-s+1)
                asum-=nums[s]
                s+=1
        return l%(len(nums)+1)