class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#------------------超时方法--------------------
        # length = len(nums)
        # for i in range(length+1):
        #     if i in nums:
        #         continue
        #     else:
        #         return i
#-----------------排序方法---------------------
        length = len(nums)
        nums.sort()
        if nums[0] != 0:     #头部处理
            return 0
        for i in range(1,length):
            if nums[i]-nums[i-1] != 1:
                return nums[i]-1
            else:
                continue 
        return nums[length-1]+1     #尾部处理
#2018.12.10
#------------------main function-------------------
if __name__ == '__main__':
    # l = [3,0,1]
    # l = [1,2,3]
    l = [0]
    s = Solution()
    print(s.missingNumber(l))