class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        fir = 0
        end = len(nums)-1
        while fir <= end:
        	mid = (fir + end)//2
        	if target == nums[mid]:
        		return mid
        	elif target > nums[mid]:
        		fir = mid + 1
        	else:
        		end = mid - 1
        #fir > end
        if nums[mid] > target:
            return mid
        #fir < end
        elif nums[mid] < target:
        	return mid + 1
#2018.11.13

#--------------------main function-----------------------
if __name__ == '__main__':
    s = Solution()
    l = [1,3,5,6]
    target = 0
    index = s.searchInsert(l,target)
    print(index)