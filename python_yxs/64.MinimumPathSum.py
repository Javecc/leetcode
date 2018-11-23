class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row == 0 or (row != 0 and len(grid[0]) == 0):
            return 0
        column = len(grid[0])
        dp = [[0 for _ in range(column)] for _ in range(row)]
        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0 and j > 0:
                    dp[i][j] =  grid[i][j] + dp[i][j-1]
                elif i > 0 and j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j] 
                else:
                     dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
            print(dp)
        print(dp)
        return dp[-1][-1]
#2018.11.23
#------------------main function-------------------
if __name__ == '__main__':
    ls = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    nums = s.minPathSum(ls)
    print(nums)
