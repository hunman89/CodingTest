class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #sort with end point
        points.sort(key=lambda x:x[1])
        arrow, cur_end = 1, points[0][1] # shot arrow to end point
        for start, end in points:
            if start > cur_end: # need 1 more arrow
                arrow += 1
                cur_end = end # change end
        return arrow