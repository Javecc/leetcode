class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #返回参数
        rlist = []
        #进行排序
        nums.sort()

        for i in range(len(nums)-3):
        	for i in range: