class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        rlist = [0 for i in range(length)]
        fir,end = 0,-1  #双指针
        for i in A:
            if i%2 == 0:
                rlist[fir] = i
                fir += 1
            else:
                rlist[end] = i
                end -= 1
        return rlist
#2018.12.17
#----------------main function------------------
if __name__ == '__main__':
    l = [3,1,2,4]
    s = Solution()
    print(s.sortArrayByParity(l))