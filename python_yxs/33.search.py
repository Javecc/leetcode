class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
        	return -1
        fir = 0
        end = len(nums)-1
        while fir <= end:
        	mid = (fir + end)//2
        	if nums[mid] == target:
        		return mid
        	elif nums[mid] < nums[end]:
        		if nums[mid] < target and target < nums[end]:
        			fir = mid + 1
        		else:
        			end = mid - 1
        	else:
        		if nums[fir] < target and target < nums[mid]:
        			end = mid - 1
        		else:
        			fir = mid + 1
        return -1
#2018.11.12


