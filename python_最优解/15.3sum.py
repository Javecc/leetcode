class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = dict()
        for i in range(len(nums)):
            tmp[nums[i]] = tmp.get(nums[i], 0) + 1
        left = sorted(filter(lambda x: x < 0, tmp))
        right = sorted(filter(lambda x: x >= 0, tmp))
        if 0 in tmp and tmp[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        for i in left:
            for j in right:
                mid = -i - j
                if mid in tmp:
                    if mid in (i, j) and tmp[mid] > 1:
                        res.append([i, mid, j])
                    elif mid < i or mid > j:
                        res.append([i, mid, j])
        return res

