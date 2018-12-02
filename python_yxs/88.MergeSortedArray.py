class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        rlist = []
        rlist[:m] = nums1[:m]
        rlist[m:m+n] = nums2[:n]
        nums1[:m+n] = sorted(rlist[:m+n])
#2018.12.02
#------------------------main function--------------------
if __name__ == '__main__':
    l1 = [1,2,3,0,0,0]
    l2 = [2,5,6]
    m = 3
    n = 3
    s = Solution()
    s.merge(l1,m,l2,n)
    print(l1) 