class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        s,e=0,len(nums)-1
        while s<e:
            m=s+(e-s)//2
            if nums[m]>nums[m+1]:
                e=m
            elif nums[m]<nums[m+1]:
                s=m+1
        return s