class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #局部峰值遍历法
        length = len(heights)
        maxarea = heights[0]  #最大面积初始值
        if length == 0:
            return maxarea
        for i in range(1,length):
            
#2018.11.30
#----------------main function------------------
if __name__ == '__main__':
    l = [2,1,5,6,2,3]
    s = Solution()
    maxarea = s.largestRectangleArea(l)
    print(maxarea)