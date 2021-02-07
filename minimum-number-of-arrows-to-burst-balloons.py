class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        points.sort(key= lambda x: x[1])
        c=1
        end=points[0][1]
        for x in points[1:]:
            if x[0]>end:
                c+=1
                end=x[1]
        return c