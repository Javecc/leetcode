class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #参数表示：
        #    接下来需要遍历的行数，列数，当前数行，列坐标，和运动方式
        def move(row,column,x,y,case):
            #递归条件:没有数时直接跳出
            if row == 0 or column == 0:
                return 
            if case == 0: #行从左往右移动
                endy = y + column #结束列坐标 = 剩余的列数 + 当前列坐标
                for i in range(y,endy):
                    rlist.append(matrix[x][i])
                row -= 1 #剩余行数-1
                x += 1   #行坐标+1
                y = endy-1 #转换列坐标
                move(row,column,x,y,1)
            elif case == 1: #列从上往下移动
                endx = x + row #结束行坐标 = 剩余的行数 + 当前行坐标
                for i in range(x,endx):
                    rlist.append(matrix[i][y])
                column -= 1 #剩余列数-1
                x = endx - 1
                y -= 1
                move(row,column,x,y,2)
            elif case == 2: #行从右往左移动
                endy = y - column #
                for i in range(y,endy,-1):
                    rlist.append(matrix[x][i])
                row -= 1
                x -= 1
                y = endy + 1
                move(row,column,x,y,3)
            elif case == 3: #列从下往上移动
            	endx = x - row
            	for i in range(x,endx,-1):
            		rlist.append(matrix[i][y])
            	column -= 1
            	x = endx + 1
            	y += 1
            	move(row,column,x,y,0)
        rlist = []
        row = len(matrix)
        if row == 0:
        	return rlist
        column = len(matrix[0]) #这句必须放在return之后
        move(row,column,0,0,0)
        return rlist
#2018.11.17

#-------------------main function-----------------------
if __name__ == '__main__':
	l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	l1 = []
	s = Solution()
	print(s.spiralOrder(l))
