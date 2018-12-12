class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minnum = -2147483649
        fir,sec,thd = minnum,minnum,minnum
        for i in range(len(nums)):
            if nums[i] > fir:
                fir,sec,thd = nums[i],fir,sec
            elif nums[i] < fir and nums[i] > sec:
                sec,thd = nums[i],sec
            elif nums[i] < sec and nums[i] > thd:
                thd = nums[i]
        if thd == minnum or thd == sec:  #表示没有第三大的数
            return fir
        else:
            return thd
#2018.12.12
#-----------------main function----------------
if __name__ == '__main__':
    # l = [2,2,3,1]
    # l = [5,2,4,1,3,6,0]
    # l = [1,2]
    # l = [5,2,2]
    l = [2,1,-2147483648]
    s = Solution()
    print(s.thirdMax(l))