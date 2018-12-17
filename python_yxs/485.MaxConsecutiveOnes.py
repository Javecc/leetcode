class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnums = 0
        x = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxnums = max(maxnums,x)
                x = 0
            else:
                x += 1
        maxnums = max(maxnums,x)
        return maxnums
#2018.12.15
#----------------main function-----------------
if __name__ == '__main__':
    l = [1,1,0,1,1,1]
    s = Solution()
    print(s.findMaxConsecutiveOnes(l))