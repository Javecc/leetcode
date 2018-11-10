class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums)-1:
        	if nums[j] == nums[j+1]:
        		j += 1
        	else:
        		i += 1
        		nums[i] = nums[j+1]
        		j += 1
        #print(set(nums))
        return len(set(nums))

#2018.11.10

#----------------主函数-------------------
if __name__ == '__main__':
	s = Solution()
	print(s.removeDuplicates([]))
