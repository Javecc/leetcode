class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i,j = 0,0  
        k = 1  #用于计数重复个数
        while j < len(nums)-1:
            if nums[j] == nums[j+1]:
                j += 1
                k += 1
            elif nums[j] != nums[j+1]:
                i += 1      #存数指针首先后移
                if k >= 2:  #表示重复数大于2
                    nums[i],nums[i+1] = nums[j],nums[j+1]
                    i += 1
                else:       #不重复，存一位数就好
                    nums[i] = nums[j+1]
                j += 1
                k = 1       #对重复数初始化
        #这种情况下，对最末尾的元素需要特殊考虑,分无重复数和有重复数
        if k >= 2 and j == len(nums)-1:
            nums[i+1] = nums[j] 
            return i+2
        else:
            return i+1
#2018.11.28
#------------------main function------------------
if __name__ == '__main__':
    # l = [1,1,1,2,2,3]
    l = [0,0,1,1,1,1,1,1,2,2,3,3]
    # l = [1,1,1,1,2,2,3]
    # l = []
    s = Solution()
    sums = s.removeDuplicates(l)
    print(sums)
    # print(l)
    for i in range(sums):
        print(l[i],end=" ")
    print("")