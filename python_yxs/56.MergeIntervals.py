# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length < 2:
        	return intervals
        #根据start进行排序
        intervals = sorted(intervals,key = lambda x: x.start)
        #return intervals
        rlist = []
        for i in range(1,length):
        	now = intervals[i]     #当前元素
        	head = intervals[i-1]  #前一元素
        	if head.end >= now.start:  #符合合并条件
        		now.start = head.start
        		now.end = max(head.end,now.end)
        	else:  #不符合合并条件
        		rlist.append(head)
        rlist.append(now)
        return rlist

#2018.11.19

#--------------------main function-----------------------
if __name__ == '__main__':
	i1 = Interval(15,18)
	i2 = Interval(1,3)
	i3 = Interval(2,6)
	i4 = Interval(8,10)
	l = [i1,i2,i3,i4]
	s = Solution()
	ls = s.merge(l)
	for i in range(len(ls)):
		print([ls[i].start,ls[i].end])