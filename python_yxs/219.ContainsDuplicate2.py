class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        booldict = {}
        for i in range(length):
            if nums[i] in booldict:
                booldict[nums[i]][0] += 1
                if i-booldict[nums[i]][1] <= k and booldict[nums[i]][0] >= 2:
                    return True
                booldict[nums[i]][1] = i  #用于改变那个数组下标
            else:
                booldict[nums[i]] = [1,i]
        return False
#2018.12.09
#-------------------main function---------------------
if __name__ == '__main__':
    # l = [1,2,3,1,2,3]
    l = [1,0,1,1]
    k = 1
    s = Solution()
    print(s.containsNearbyDuplicate(l,k))