class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rlist = []
        for i in range(numRows):
            rlist.append([])
            for j in range(i+1):
                if j == 0 or i == j:
                    rlist[i].append(1)
                else:
                    sums = rlist[i-1][j] + rlist[i-1][j-1]
                    rlist[i].append(sums)
        return rlist
#2018.12.03
#------------------main function-------------------
if __name__ == '__main__':
    num = 5
    s = Solution()
    print(s.generate(num))