class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = 0
        if length == 0:
            return
        for i in range(length):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k,length):
            nums[i] = 0
#2018.12.11
#------------------main function--------------------
if __name__ == '__main__':
    l = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(l)
    print(l)