"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=self.sorting_key)
        first = 0
        second = 1

        while second < len(intervals):
            if intervals[first].end > intervals[second].start:
                return False
            first += 1
            second += 1
        return True

    def sorting_key(self, intervals: List[Interval]):
        return intervals.start





















        
        # intervals.sort(key=lambda x: x.start)
        # first_idx = 0
        # second_idx = 1

        # while second_idx < len(intervals):
        #     if intervals[first_idx].end > intervals[second_idx].start:
        #         return False
                
        #     first_idx += 1
        #     second_idx += 1
        # return True

