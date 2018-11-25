class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        templist = []
        row = len(matrix)
        if row == 0:
            return False
        column = len(matrix[0])
        if column == 0:
            return False
        for i in range(row):
            for j in range(column):
                templist.append(matrix[i][j])
        # print(templist)
        fir = 0
        end = len(templist)-1
        while(fir <= end):
            mid = (fir + end)//2
            if templist[mid] == target:
                return True
            elif templist[mid] > target:
                end = mid-1
            else:
                fir = mid+1
        return False
#2018.11.25
#-----------------main function-------------------
if __name__ == '__main__':
    ls = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 13
    s = Solution()
    print(s.searchMatrix(ls,target))
    