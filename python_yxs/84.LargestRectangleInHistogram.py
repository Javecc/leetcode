class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
#---------------------------------------------------
        #局部峰值遍历法(超时)
        # length = len(heights)
        # if length == 0:
        #     return 0
        # maxarea = heights[0]  #最大面积初始值
        # for i in range(1,length):
        #     minH = heights[i]
        #     for j in range(i,-1,-1):
        #         minH = min(minH,heights[j])
        #         maxarea = max(maxarea,minH*(i-j+1))
        # return maxarea
#----------------------------------------------------
        #局部峰值遍历法(有效,但效率低)
        length = len(heights)
        if length == 0:
            return 0
        maxarea = heights[0]
        for i in range(0,length):
            if i < length-1 and heights[i] <= heights[i+1]:
                continue
            minH = heights[i]
            for j in range(i,-1,-1):
                minH = min(minH,heights[j])
                maxarea = max(maxarea,minH*(i-j+1))
        return maxarea
#---------------------------------------------------
        #栈方法
        
#2018.11.30
#----------------main function------------------
if __name__ == '__main__':
    # l = [2,1,5,6,2,3]
    l = [1,1]
    s = Solution()
    maxarea = s.largestRectangleArea(l)
    print(maxarea)