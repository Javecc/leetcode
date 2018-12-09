class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        booldict = {}
        length = len(nums)
        if length==0:
            return False
        for i in range(length):
            if nums[i] in booldict:
                booldict[nums[i]] += 1
            else:
                booldict[nums[i]] = 1
        for i in booldict:
            if booldict[i] >= 2:
                return True
        return False
#2018.12.09
#---------------------main function---------------------
if __name__ == '__main__':
    # l = [1,2,3,1]
    l = [1,2,3,4]
    s = Solution()
    print(s.containsDuplicate(l))