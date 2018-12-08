class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==0:
            return
        start = 0
        k %= n
        while k%n:
            for i in range(start,start+k):
                nums[i],nums[n-k+i] = nums[n-k+i],nums[i]
            n -= k
            start = i + 1
            k %= n
#2018.12.08
#-----------------main function-------------------
if __name__ == '__main__':
    # l = [1,2,3,4,5,6,7]
    l = [1,2]
    k = 3
    s = Solution()
    s.rotate(l,k)
    print(l)