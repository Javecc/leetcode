class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #时间换空间
        zerolistx = []  #记录为0的行号
        zerolisty = []  #记录为0的列号
        row = len(matrix)
        if row == 0:
            return []
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    zerolistx.append(i)
                    zerolisty.append(j)
        for i in range(row):
            for j in range(column):
                if i in zerolistx:
                    matrix[i][j] = 0
                elif j in zerolisty:
                    matrix[i][j] = 0
        return matrix
#2018.11.24
#------------------main function------------------
if __name__ == '__main__':
    # l = [[1,1,1],[1,0,1],[1,1,1]]
    l = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s = Solution()
    print(s.setZeroes(l))