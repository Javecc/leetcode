class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return
        for i in range(length-1):
            for j in range(i,length):
                if nums[j] < nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
#2018.11.26
#----------------main function-----------------
if __name__ == '__main__':
    l = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(l)
    print(l)