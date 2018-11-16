class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dynasum = 0
        maxsum = nums[0]
        for i in range(len(nums)):
        	dynasum += nums[i]
        	maxsum = max(maxsum,dynasum)
        	if dynasum < 0:
        		dynasum = 0
        return maxsum
#2018.11.16

#----------------main function------------------
if __name__ == '__main__':
	l = [2,-1,3,-4,3,2,-2,5]
	s = Solution()
	print(s.maxSubArray(l))