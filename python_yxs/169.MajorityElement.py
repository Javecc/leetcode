class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        majnum = 0  #众数个数
        num = 0     #众数
        l = {}
        for i in range(length):
            if nums[i] in l:
                l[nums[i]] += 1
            else:
                l[nums[i]] = 1
        # 用于求众数个数
        # for j in l:
        #     majnum = max(majnum,l[j])
        # return majnum
        for j in l:
            if l[j] > majnum:
                majnum = l[j]
                num = j
        return num
#2018.12.07
#-------------------main function-------------------
if __name__ == '__main__':
    # l = [3,2,3]
    # l = [2,2,1,1,1,2,2]
    l = [1,2,3,4,5,6,5]
    s = Solution()
    print(s.majorityElement(l))