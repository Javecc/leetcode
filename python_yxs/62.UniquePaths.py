class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
#2018.11.22
        
#---------------main function-------------------
if __name__ == '__main__':
    m = 3
    n = 2
    s = Solution()
    nums = s.uniquePaths(m,n)
    print(nums)

    # dp = [[1 for _ in range(3)] for _ in range(2)]
    # for i in range(1,2):
    #     for j in range(1,3):
    #         dp[i][j] = dp[i][j-1] + dp[i][j-1] 
    # print(dp[-1][-1])