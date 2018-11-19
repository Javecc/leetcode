class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #length = len(nums)-1
        #maxpos = 0 #能够到达的最远点  #[3,2,1,0,4]
        length = len(nums)
        maxpos = nums[0]
        for i in range(length):
        	#如果当前位置大于最远点，表示无法到达
        	if i > maxpos:
        		return False
        	maxpos = max(maxpos,i+nums[i])
        #加判断:大于等于其坐标最大值
        if maxpos >= length-1:
        	return True
#2018.11.18

#-------------------main function--------------------------
if __name__ == '__main__':
	#l = [3,2,1,0,4]
	l = [3,2,1,0,4]
	s = Solution()
	print(s.canJump(l))

