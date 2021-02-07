class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e=0,len(nums)-1
        if nums[s]<=nums[e]:
            return nums[s]
        while s<=e:
            m=s+(e-s)//2
            if nums[m]<nums[m-1]:
                return nums[m]
            if nums[m]<nums[e]:
                e=m
            else:
                s=m+1