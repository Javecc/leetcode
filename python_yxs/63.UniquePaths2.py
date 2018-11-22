class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        #需要考虑特殊情况就是只有一行或者一列下有障碍物的情况，这种情况下路径数为0
        if (row != 0 and obstacleGrid[0][0] == 1) or (row == 1 and 1 in obstacleGrid[0]):
            return 0
        column = len(obstacleGrid[0])
        if column == 1:
            for i in range(row):
                if obstacleGrid[i][0] == 1:
                    return 0
        for i in range(row):
            for j in range(column):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = 0
        for i in range(1,row):
            for j in range(1,column):
                if obstacleGrid[i][j] == 0:
                    continue
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
#2018.11.22
#------------------main function-----------------
if __name__ == '__main__':
    # ls = [[0,0,0],[0,1,0],[0,0,0]]
    ls = [[0,0],[1,1],[0,0]]
    s = Solution()
    nums = s.uniquePathsWithObstacles(ls)
    print(nums)