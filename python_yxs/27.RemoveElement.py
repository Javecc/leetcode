class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = nums.count(val)
        l = len(nums)
        while val in nums:
        	nums.removeElement(val)
        return l-n
#2018.11.10
