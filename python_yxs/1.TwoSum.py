class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        fir = 0
        end = len(nums) - 1
        nums.sort()
        while fir <= end:
        	temp = nums[fir] + nums[end]
        	if temp == target:
        		return [fir,end]
        	elif temp < target:
        		fir += 1
        	else:
        		end -= 1
#2018.11.13

#---------------main function----------------
if __name__ == '__main__':
	s = Solution()
	li = [3,2,4]
	target = 6
	re = s.twoSum(li,target)
	print(re)