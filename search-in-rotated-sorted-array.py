class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        while s<e:
            m=s+(e-s)//2
            if nums[m]>nums[e]:
                s=m+1
            else:
                e=m
        r=s
        s,e=0,len(nums)-1
        while s<=e:
            m=s+(e-s)//2
            rm=(m+r)%len(nums)
            if nums[rm]==target:
                return rm
            if nums[rm]<target:
                s=m+1
            else:
                e=m-1
        return -1