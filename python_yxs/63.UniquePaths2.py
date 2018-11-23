class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        if row == 0 or obstacleGrid[0][0] == 1 or (row != 0 and len(obstacleGrid[0]) == 0):
            return 0
        column = len(obstacleGrid[0])
        dp = [[0 for _ in range(column)] for _ in range(row)]
        for i in range(row):
            for j in range(column):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
#2018.11.22
#------------------main function-----------------
if __name__ == '__main__':
    ls = [[0,0,0],[0,1,0],[0,0,0]]
    # ls = [[0,0],[1,1],[0,0]]
    # ls = [[0,0],[1,0]]
    # ls = [[0,0],[0,1]]
    # ls = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    s = Solution()
    nums = s.uniquePathsWithObstacles(ls)
    print(nums)