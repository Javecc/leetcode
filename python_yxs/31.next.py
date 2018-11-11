class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0:
        	#右边数比左边小，没有相邻情况则跳过
        	if nums[i] <= nums[i-1]:
        		i -= 1
        	elif nums[i] > nums[i-1]:
		        for j in range(len(nums)-1,i-1,-1):
		        	if nums[j] > nums[i-1]:
		        		nums[i-1],nums[j] = nums[j],nums[i-1]
		        		break
		        break
        nums[i:] = reversed(nums[i:])
#2018.11.11

#-------------------测试主函数-------------------
if __name__ == '__main__':
	l = Solution()
	li = [1,2,4,6,5,3]
	l.nextPermutation(li)
	print(li)